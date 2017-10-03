import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class PageRank{
  public static void main(String[] args) throws Exception{
	  int iterations = 3;
	  
	  if (args.length != 2){
		  System.err.println("Usage: PageRank <input path> <output path>");
		  System.exit(-1);
	  }
	  Configuration conf = new Configuration();
	  conf.set("mapred.textoutputformat.separator", " ");
	  
	  // Finds the output parent directory
	  if(args[1].charAt(args[1].length() -1 ) == '/') {
		  args[1] = args[1].substring(0, args[1].length() - 2);
	  }
	  String parentdir = args[1].substring(0, args[1].lastIndexOf('/') + 1);
	  String inputTemporary = args[0];
	  String outputTemporary;
	  int  i = 0;
	  boolean success = false;
	  while(i < iterations){
		  if(i != 0) { // after the first iteration
			  inputTemporary = parentdir + "output"+String.valueOf(i-1);
		  }
		  if(i == iterations - 1) { // last iteration
			  outputTemporary = args[1];
		  }else{
			  outputTemporary = parentdir + "output"+String.valueOf(i);
		  }    	
		  Job job = new Job(conf);
		  job.setNumReduceTasks(1);
		  job.setJarByClass(PageRank.class);
		  job.setJobName("Page Rank Iterative");

		  FileInputFormat.addInputPath(job, new Path(inputTemporary));
		  FileOutputFormat.setOutputPath(job, new Path(outputTemporary));

		  job.setMapperClass(PageRankMapper.class);
		  job.setReducerClass(PageRankReducer.class);

		  job.setOutputKeyClass(Text.class);
		  job.setOutputValueClass(Text.class);
		  success = job.waitForCompletion(true); // makes sure the job completes
		  if(!success) {
			  System.exit(1);
		  }
		  i += 1;
	  }
	  System.exit(0);
  	}
}