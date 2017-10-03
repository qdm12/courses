import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class PageRankMapper extends Mapper<LongWritable, Text, Text, Text>{
	private static final char separator = ' ';
	
	@Override
	public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException{
		String line = value.toString();

		// Source
		// Because source and others may be separated by more than one space:
		int indexA = line.indexOf(separator);
		int indexB = indexA + 1;
		for(int i=indexA+1; i<line.length(); i++){
			if(line.charAt(i) != separator) {
				indexB = i;
				break;
			}    	
		}
		String source = line.substring(0, indexA);
		line = line.substring(indexB);

		// PR
		float PR = Float.parseFloat(line.substring(line.lastIndexOf(separator)+1));
		indexB = line.lastIndexOf(separator);
		if(indexB < 0) { // no outlinks, only a source and a PR value
			line = "";
		}else {
			line = line.substring(0, indexB);
		}
		
		// Outlink targets
		List<String> outlink_targets = new ArrayList<String>();
		int start = 0;
		for(int i=0; i<line.length(); i++){
			if(line.charAt(i) == separator) {
				outlink_targets.add(line.substring(start, i));
				start = i + 1;
			}else if(i == line.length() - 1) {
				outlink_targets.add(line.substring(start));
			}
		}

		// PR per outlink
		float PRperLink = PR; // if there is 0 or 1 outlink, then it's PR
		if(outlink_targets.size() > 1) {
			PRperLink /= outlink_targets.size();
		}
		
		
		// Writing to Reducers
		String value_output = "";
		// Writes the PR information
		for(String target : outlink_targets){
			value_output = source + Character.toString(separator) + Float.toString(PRperLink);
			context.write(new Text(target), new Text(value_output));
		}
		
		// Writes the original information
		value_output = "";
		if(!outlink_targets.isEmpty()){ // (source, targets)
			for(String target : outlink_targets) {
				value_output += target + ' ';
			}
			value_output = value_output.trim();
		}else { // (source, PR) - uncommon case
			value_output = Float.toString(PR);
		}
		context.write(new Text(source), new Text(value_output));	
	}
}