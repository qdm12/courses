import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class TweetCounterMapper extends Mapper<LongWritable, Text, Text, IntWritable>{
  private static final List<String> search_terms = Arrays.asList("hackathon", "Dec", "Chicago", "Java");
  @Override
  public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException{
    String line = value.toString().toLowerCase();
    int found;
    for(String term : search_terms){
        if(line.contains(term.toLowerCase())){
            found = 1;
        }else{
            found = 0;
        }
        context.write(new Text(term), new IntWritable(found));
    }
  }
}