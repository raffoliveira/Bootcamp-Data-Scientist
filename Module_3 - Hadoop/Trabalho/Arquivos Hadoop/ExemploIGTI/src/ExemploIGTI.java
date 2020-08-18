package IGTI;

import java.io.*;
import java.util.*;
import java.util.Random;
import java.text.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;


public class ExemploIGTI extends Configured implements Tool 
{          
    public static void main (final String[] args) throws Exception {   
      int res = ToolRunner.run(new Configuration(), new ExemploIGTI(), args);        
      System.exit(res);           
    }   

    public int run (final String[] args) throws Exception {
      try{ 	             	       	
            JobConf conf = new JobConf(getConf(), ExemploIGTI.class);			
            conf.setJobName("Exemplo IGTI - Media");            
               
            final FileSystem fs = FileSystem.get(conf); 
            Path diretorioEntrada = new Path("Entrada"), diretorioSaida = new Path("Saida");            

            /* Criar um diretorio de entrada no HDFS */
            if (!fs.exists(diretorioEntrada))
                fs.mkdirs(diretorioEntrada);

            /* Adicionar um arquivo para ser processado */
            fs.copyFromLocalFile(new Path("/usr/local/hadoop/Dados/arquivoBigData.txt"), diretorioEntrada);             

            /* Atribuindo os diretorios de Entrada e Saida para o Job */
            FileInputFormat.setInputPaths(conf,  diretorioEntrada); 
            FileOutputFormat.setOutputPath(conf, diretorioSaida);
  
            conf.setOutputKeyClass(Text.class);     
            conf.setOutputValueClass(Text.class);   
            conf.setMapperClass(MapIGTI.class);
            conf.setReducerClass(ReduceIGTI.class);
            JobClient.runJob(conf);   
                                          
        }
        catch ( Exception e ) {
            throw e;
        }
        return 0;
     }
 
    public static class MapIGTI extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {
            
      public void map(LongWritable key, Text value, OutputCollector<Text, Text> output, Reporter reporter)  throws IOException {

            Text txtChave = new Text();
            Text txtValor = new Text();
             
            String codigoCliente = value.toString().substring(58, 61);
            String qtdeItens = value.toString().substring(76, 84);

            txtChave.set(codigoCliente);
            txtValor.set(qtdeItens);                       
            
            output.collect(txtChave, txtValor);            

                       
      }        
    }
 
   
    public static class ReduceIGTI extends MapReduceBase implements Reducer<Text, Text, Text, Text> {       
      
       public void reduce (Text key, Iterator<Text> values, OutputCollector<Text, Text> output, Reporter reporter) throws IOException {                                                                                 double media = 0.0; 
            int acumuladorItens = 0, contaVendas = 0;
            Text value = new Text();
        
            while (values.hasNext()) {
                value = values.next();               
                contaVendas++;
                acumuladorItens += Integer.parseInt(value.toString());
            }            
            media = acumuladorItens / new Double(contaVendas);
                          
            value.set(String.valueOf(media)); 
            output.collect(key, value);           
      }            
    
    }
}






