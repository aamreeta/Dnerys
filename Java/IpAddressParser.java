/**
 * Author: Amrita Gautam
 * email: aamreeta@gmail.com
 */
import java.util.ArrayList;
import java.util.List;

public class IpAddressParser {
	
   /**
    * Checks the validity of an input string
    * An valid input String is has length >= 4 and <=12 and is not null
    * @param validInputString 
    * @return                  true if the input string is valid 
    */
	public boolean validateInput(String validInputString) {
		
		 if(validInputString==null || validInputString.length()<4 || validInputString.length()>12)
			 return false;
		
		return true;
	}
	/**
	 * This method returns a list of IP address strings that are possible 
	 * to derive from different combinations of the input string.
	 * An valid input String has length >= 4 and <=12
	 * 
	 * @param  inputStr  The input string from which combinations of valid IP Addresses is to be generated 
	 * @return           Returns the List of valid IP Address combinations, Returns empty list for invalid input string 
	 *                   or if no valid IP address can be generated from the input string.
	 */
	public List<String> getIPAddressList(String inputStr){
		/**
		 * A valid IP Address has four substrings separated by "." (dot)
		 * Ex: 127.0.0.0 /23.128.33.1
		 * The integer value of each such substring has to less than 255.
		 * Ex: 255.255.255.255 is the largest value of an IP Address numerically.
		 * Some ex of invalid IP Address combinations are 265.1.1.1/127.365.56.10/12.34.657.45
		 * 
		 * To generate valid IP address from an input string ,the input is divided into four buckets.
		 * The programs scans through the input and generates substrings of the input string for each bucket.
		 * A valid bucket contains a substring of max length 3 and integer value < 255.
		 * If all the four buckets meet this requirement the ,a valid IP address is constituted by concatenating 
		 * substrings from all the four buckets and adding "." between them.
		 *  
		 */
		List<String> validIpAddressList=new ArrayList<String>();
		int MX_BUCKET_LEN=3;
	    if(validateInput(inputStr)){
			//For loop for Bucket 1
	    	for(int i=1;i<MX_BUCKET_LEN+1;i++){
				String bucketOne=inputStr.substring(0,i);
				if(isValid(bucketOne)){
					//For loop for Bucket 2
					for(int j=1;j<MX_BUCKET_LEN+1 && i+j<inputStr.length();j++){
						String bucketTwo=inputStr.substring(i,i+j);
						if(isValid(bucketTwo)){
							//For loop for bucket 3 and bucket 4
							for(int k=1;k<MX_BUCKET_LEN+1 && i+j+k<inputStr.length();k++){
								String bucketThree=inputStr.substring(i+j,i+j+k);
								String bucketFour=inputStr.substring(i+j+k);
								if(isValid(bucketThree)&&isValid(bucketFour)){
									validIpAddressList.add(bucketOne+"."+bucketTwo+"."+bucketThree+"."+bucketFour);
								}
								
							}
						}
						
					}
					
				}
			}
	    
			
		}
		
		return validIpAddressList;
		
	}
		
	
	/**
	 * Determines the validity of substring in a bucket
	 * The length of the bucket needs to be < 3 and integer value < 255
	 * @param bucketOne  The substring in a bucket
	 * @return           Returns true if the substring meets requirements
	 */
	private boolean isValid(String bucketOne) {
		int bucketOneIntVal=new Integer(bucketOne).intValue();
		if(bucketOneIntVal<=255)
		return true;
		else 
		return false;
	}
	
		
}
