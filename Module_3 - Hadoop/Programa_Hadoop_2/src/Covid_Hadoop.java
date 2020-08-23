package covid_hadoop;

import java.io.*;
import java.util.*;
import java.util.Random;
import java.util.Arrays;
import java.text.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

public class Covid_Hadoop extends Configured implements Tool 
{          
    public static void main (final String[] args) throws Exception {   
      int res = ToolRunner.run(new Configuration(), new Covid_Hadoop(), args);        
      System.exit(res);           
    }   

    public int run (final String[] args) throws Exception {     
        try{ 	             	       	
            JobConf conf = new JobConf(getConf(), Covid_Hadoop.class);
            conf.setJobName("Covid19_Calculus"); //instanciando o job de serviço do hadoop

            conf.setStrings("execution", Integer.toString(337)); //usado para enviar dados para a classe mapper e reducer

            final FileSystem fs = FileSystem.get(conf); //objeto para manipular o hdfs

            /*
            fs.exists = verifica se determinado caminho existe
            fs.getHomeDirectory = retorna diretorio raiz do HDFS
            fs.isDirectory = verifica se caminho p eh diretorio
            fs.isFile = verifica se p eh arquivo
            fs.mkdirs = cria diretorio
            fs.delete = deleta diretorio*/

            //configurando caminho do diretorio de entrada e saida de arquivos
            Path entry_directory = new Path("/user/hadoop/input/EntryFolder"), exit_directory = new Path("/user/hadoop/output/ExitFolder");
            
            //cria o diretorio de entrada. O de saída o hadoop cria automatico
            if(fs.exists(entry_directory)){
              System.out.println("Directory EntryFolder already exist!!!");
              fs.delete(entry_directory);
	      fs.mkdirs(entry_directory); 
	      System.out.println("Directory EntryFolder created!!!");
            }
            else{
              System.out.println("Directory EntryFolder created!!!");
              fs.mkdirs(entry_directory); 
            }
            
            //move o arquivo para dentro do hdfs
            fs.copyFromLocalFile(new Path("/home/hadoop/hadoop2.9.2/files_data/WHO-COVID-19-global-data.csv"), entry_directory);
            
            //criando os diretorios  de entrada e saída
            FileInputFormat.setInputPaths(conf, entry_directory);

            if(fs.exists(exit_directory)){
              System.out.println("Directory ExitFolder already exist!!!");
              fs.delete(exit_directory);
	      FileOutputFormat.setOutputPath(conf, exit_directory); 
	      System.out.println("Directory ExitFolder created!!!");
            }
            else{
              FileOutputFormat.setOutputPath(conf, exit_directory); 
              System.out.println("Directory ExitFolder created!!!");              
            }             

            //FileOutPutFormat.getInputPaths = retorna uma lista de diretorios

            conf.setOutputKeyClass(Text.class);
            conf.setOutputValueClass(Text.class);

            conf.setMapperClass(MapCovid.class);
            //conf.setCombinerClass(ReduceCovid.class); //utilizada como um pre-reducer. Minimiza o numero de processamento
            conf.setReducerClass(ReduceCovid.class);
            
            JobClient.runJob(conf);
        }
        catch ( Exception e ) {
            throw e;
        }
        return 0;
     }
 
    public static class MapCovid extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {       
      
      public void configure(JobConf job){
        System.out.println(job.getStrings("execution"));
      }

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
	
        output.collect(txtKey, txtValue); //coleta as chaves e valores mapeados                
      } 
      
      public void close(){
        System.out.println("Processing Mapper finished.");
      }
    }
   
    public static class ReduceCovid extends MapReduceBase implements Reducer<Text, Text, Text, Text> {   
    
      public void configure(JobConf job){
        System.out.println(job.getStrings("execution"));
      }

      //reduce executa de acordo com o numero de chaves do arquivo
      public void reduce (Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {                                                                                 double media = 0.0; 
        
        String[] field = new String[3];
        Text value = new Text();
        int biggerCases = 0, biggerDeaths = 0;
        String countryCases = "", countryDeaths = "", strExit = "";

        while(values.hasNext()){
            value = values.next();
            field = value.toString().split("\\|");
	    System.out.println(Arrays.toString(field));
	    	    
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

      public void close(){
        System.out.println("Processing Reducer finished.");
      }
    
    }
}






