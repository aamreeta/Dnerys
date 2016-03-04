/**
 * Author: Amrita Gautam
 * email: aamreeta@gmail.com
 */
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.List;

import org.junit.Before;
import org.junit.Test;

public class IpAddressParserTest {
	IpAddressParser ipParsser;
	
	@Before
	public void init(){
		ipParsser=new IpAddressParser();
	}

	
	/**
	 * Test the getIPAddressList() with shortest valid input string of length 4
	 * There result can be only be one valid IP Address
	 */
	@Test
	public void testGetIPAddressListShortString(){
		String shortInputtString="1234";
		String expectedResult="1.2.3.4";
		List<String> resultList=ipParsser.getIPAddressList(shortInputtString);
		assertTrue(resultList.size()==1);
		assertTrue((resultList.get(0)).equals(expectedResult));
		
	}
	/**
	 * Test the getIPAddressList() with longest valid input string of length 12
	 * There result can be only be one valid IP Address
	 */
	@Test
	public void testGetIPAddressListLongString(){
		String longInputtString="123234255127";
		String expectedResult="123.234.255.127";
		List<String> resultList=ipParsser.getIPAddressList(longInputtString);
		assertTrue(resultList.size()==1);
		assertTrue((resultList.get(0)).equals(expectedResult));
		
	}
	/**
	 * Tests the results of an input string of length >4 and <12
	 */
	@Test
	public void testGetIPAddressListRegularString(){
		String longInputtString="1234567";
		List<String> expectedResult=new ArrayList<String>();
		expectedResult.add("1.23.45.67");
		expectedResult.add("1.234.5.67");
		expectedResult.add("1.234.56.7");
		expectedResult.add("12.3.45.67");
		expectedResult.add("12.34.5.67");
		expectedResult.add("12.34.56.7");
		expectedResult.add("123.4.5.67");
		expectedResult.add("123.4.56.7");
		expectedResult.add("123.45.6.7");
	
		List<String> resultList=ipParsser.getIPAddressList(longInputtString);
		assertTrue(resultList.size()==9);
		for(String result:resultList){
			assertTrue(expectedResult.contains(result));
		}
		
		
	}
	
	/**
	 * Tests the results of the getIPAddressList() for an invalid input string 
	 */
	@Test 
	public void testGetIPAddressListInvalidString(){
		String shortInputtString="123";
		String longInputString="1234567891234";
		List<String> resultList=ipParsser.getIPAddressList(shortInputtString);
		assertTrue(resultList.size()==0);
		resultList=ipParsser.getIPAddressList(longInputString);
		assertTrue(resultList.size()==0);
		
	}
	
	/**
	 * Tests the results of the getIPAddressList() for an valid input string 
	 * from which no valid IP address can be generated.
	 */
	@Test 
	public void testGetIPAddressListNoResult(){
		
		String inputString="123456789123";
		List<String> resultList=ipParsser.getIPAddressList(inputString);
		assertTrue(resultList.size()==0);
		
		
		
	}
	/**
	 * Test the validateInput() with  valid input string of length >= 4 and <12
	 * 
	 */
	@Test
	public void testValidInput() {
		String validInputString1="1234";
		assertTrue(ipParsser.validateInput(validInputString1));
		String validInputString2="123456";
		assertTrue(ipParsser.validateInput(validInputString2));
	}
	
	/**
	 * Test the validateInput() with invalid input string of length < 4
	 * 
	 */
	@Test
	public void testInvalidInputShort() {
		String invalidInputString="12";
		
		assertFalse("The input string is too short for an IP Address",ipParsser.validateInput(invalidInputString));
	}
	
	/**
	 * Test the validateInput() with invalid input string of length >12 
	 * 
	 */
	@Test
	public void testInvalidInputLong() {
		String invalidInputString="1271271271271";
		assertFalse("The input string is too long for an IP Address",ipParsser.validateInput(invalidInputString));
		
	}
	/**
	 * Test the validateInput() with null input string 
	 * 
	 */
	@Test
	public void testInvalidInputNull() {
		String invalidInputString=null;
		assertFalse("The input string is null",ipParsser.validateInput(invalidInputString));
		
	}
		
	}


