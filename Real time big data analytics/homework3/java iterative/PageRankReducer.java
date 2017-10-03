import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class PageRankReducer extends Reducer<Text, Text, Text, Text>{
	private static final char separator = ' ';
	
	@Override
	public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException{
		String value_input;
		String value_output = "";
		float PR = 0;
		int index;
		for (Text value : values){
			value_input = value.toString().trim();
			int countSpaces = value_input.length() - value_input.replace(" ", "").length();
			if(countSpaces != 1) {
				try {
					PR = Float.parseFloat(value_input);
				} catch (NumberFormatException e) {
					value_output = value_input + ' '; // targets of key (source)
				}
			}else{
				String test = value_input.split(" ")[1]; // source, PRperLink or other
				float PRperLink = 0;
				boolean originalData = false;
				try {
					PRperLink = Float.parseFloat(test);
				} catch (NumberFormatException e) {
					originalData = true;
					value_output = value_input + ' '; // targets of key (source)
				}
				if(!originalData) {
					PR += PRperLink;
				}
			}
		}
		value_output += Float.toString(PR);
		context.write(key, new Text(value_output));
	}
}