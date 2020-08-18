package covid_hadoop;

import java.io.*;
import java.util.*;
import java.util.Random;
import java.text.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;
import org.w3c.dom.Text;


public class Covid_Hadoop extends Configured implements Tool 
{          
    public static void main (final String[] args) throws Exception {   
      int res = ToolRunner.run(new Configuration(), new Covid_Hadoop(), args);        
      System.exit(res);           
    }   

    public int run (final String[] args) throws Exception {
     
        try{ 	             	       	
            JobConf conf = new JobConf(getConf(), Covid_Hadoop.class);
            conf.setJobName("Cálculo Covid19"); //instanciando o job de serviço do hadoop

            final FileSystem fs = FileSystem.get(conf); //objeto para manipular o hdfs

            //configurando caminho do diretorio de entrada e saida de arquivos
            Path entry_directory = new Path("/user/hadoop/input/EntryFolder"), exit_directory = new Path("/user/hadoop/output/ExitFolder");
            //cria o diretorio de entrada. O de saída o hadoop cria automatico
            fs.mkdirs(entry_directory); 
            //move o arquivo para dentro do hdfs
            fs.copyFromLocalFile(new Path("/home/hadoop/hadoop2.9.2/files_data/WHO-COVID-19-global-data.csv"), entry_directory);
            //criando os diretorios 
            FileInputFormat.setInputPaths(conf, entry_directory);
            FileOutputFormat.setOutputPath(conf, exit_directory);

            conf.setOutputKeyClass(Text.class);
            conf.setOutputValueClass(Text.class);

            conf.setMapperClass(MapCovid.class);
            conf.setReducerClass(ReduceCovid.class);

            JobClient.runJob(conf);
        }
        catch ( Exception e ) {
            throw e;
        }
        return 0;
     }
 
    public static class MapCovid extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {            
      public void map(LongWritable key, Text value, OutputCollector<Text, Text> output, Reporter reporter)  throws IOException {
        
        Text txtKey = new Text();
        Text txtValue = new Text();

        //value eh cada linha do arquivo. Se o arquivo tem 1000 linhas o map lê 1000 vezes
        //logo estou lendo o arquivo e armazenando cada linha em um vetor
        String[] dataCovid = value.toString().split(";");
        String dataEvent = dataCovid[0];
        String countryEvent = dataCovid[2];
        int newsCases = Integer.parseInt(dataCovid[4]);
        int newsDeaths = Integer.parseInt(dataCovid[6]);

        String strKey = dataEvent;
        String strValue = countryEvent + "|" + String.valueOf(newsCases) + "|" + String.valueOf(newsDeaths);

        txtKey.set(strKey);
        txtValue.set(strValue);

        output.collect(txtKey, txtValue);                        
      }        
    }
   
    public static class ReduceCovid extends MapReduceBase implements Reducer<Text, Text, Text, Text> {         
      public void reduce (Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {                                                                                 double media = 0.0; 
        
        String[] field = new String[3];
        Text value = new Text();
        int biggerCases = 0, biggerDeaths = 0;
        String countryCases = "", countryDeaths = "", strExit = "";

        while(values.hasNext()){
            value = values.next();
            field = value.toString().split("\\|");
            
            if(Integer.parseInt(field[1]) > biggerCases){
                biggerCases = Integer.parseInt(field[1]);
                countryCases = field[0];
            }
            if(Integer.parseInt(field[2]) > biggerDeaths){
                biggerDeaths = Integer.parseInt(field[2]);
                countryDeaths = field[0];
            }
        }
        strExit = "Cases: " + String.valueOf(biggerCases) + " in " + countryCases + ".\n";
        strExit += "Deaths: " + String.valueOf(biggerDeaths) + " in " + countryDeaths + ".";

        value.set(strExit);
        output.collect(key, value);
      }            
    
    }
}






