import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class MaxTemperatureMapper extends Mapper<LongWritable, Text, Text, IntWritable>{
  private static final int MISSING = 9999;
  @Override
  public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException{
    String line = value.toString();
    String year = line.substring(15, 19);
    int airTemperature;
    if (line.charAt(40) == '+'){ // parseInt doesn't like leading plus signs
      airTemperature = Integer.parseInt(line.substring(41, 45));
    } else{
      airTemperature = Integer.parseInt(line.substring(40, 45));
    }
    String quality = line.substring(45, 46);
    if (airTemperature != MISSING && quality.matches("[01459]")){
      context.write(new Text(year), new IntWritable(airTemperature));
    }
  }
}