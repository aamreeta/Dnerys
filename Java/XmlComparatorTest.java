/**
 * Author: Amrita Gautam
 * email: aamreeta@gmail.com
 */
import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class XmlComparatorTest {
	XmlComparator xmlComparator;
	
	@Before
	public void init(){
		 xmlComparator=new XmlComparator();
	}
    /**
     * Test isXmlEqual() with simple identical xmls
     * Two xmls are considered identical if the content and sequence of the nodes in the documents are exactly the same.
     */
	@Test
	public void testSimpleIdenticalXmls() {
		String xml1="<node att=\"1\">test</node>";
		String xml2="<node att=\"1\">test</node>";
		assertTrue(xmlComparator.isXmlEqual(xml1, xml2));
		
	}
	/**
     * Test isXmlEqual() with nested identical xmls
     * Two xmls are considered identical if the content and sequence of the nodes in the documents are exactly the same.
     */
	@Test
	public void testNestedIdenticalXmls(){
		String xml1="<?xml version=\"1.0\"?> <node> <element att1=\"a\" att2=\"b\"/><element>Test</element></node>";
		String xml2="<?xml version=\"1.0\"?> <node> <element att1=\"a\" att2=\"b\"/><element>Test</element></node>";
		assertTrue(xmlComparator.isXmlEqual(xml1, xml2));
	}
	
	/**
	 * Test isXmlEqual() with simple similar xmls
	 * Two xmls are considered similar if the content of the nodes in the documents are the same, but some minor differences exist 
	 * e.g. sequencing of sibling elements, values of namespace prefixes, use of implied attribute values
	 */
	
	@Test 
	public void testSimpleSimilarXmls(){
		String xml1="<node att1=\"1\" att2=\"2\">test</node>";
		String xml2="<node att2='2' att1='1'>test</node>";
		assertTrue(xmlComparator.isXmlEqual(xml1, xml2));
	}
	
	/**
	 * Test isXmlEqual() with nested similar xmls
	 * Two xmls are considered similar if the content of the nodes in the documents are the same, but some minor differences exist 
	 * e.g. sequencing of sibling elements, values of namespace prefixes, use of implied attribute values
	 */
	@Test 
	public void testNestedSimilarXmls(){
		String xml1="<?xml version=\"1.0\"?>"+"\n"+"<node> <element att1=\"a\" att2=\"b\"/><element>Test</element></node>";
		String xml2="<?xml "+"\n"+"version=\"1.0\"?> <node><element att2='b\' att1='a\' /> <element>Test</element></node>";
		assertTrue(xmlComparator.isXmlEqual(xml1, xml2));
	}
	
	/**
	 * 
	 * Test isXmlEqual() with simple different xmls.
	 * 
	 */
	@Test
	public void testSimpleDifferentXmls() {
		String xml1="<node att=\"1\">test</node>";
		String xml2="<node att=\"1\">test2</node>";
		assertFalse(xmlComparator.isXmlEqual(xml1, xml2));
		
	}
	
	/**
	 * 
	 * Test isXmlEqual() with nested different xmls.
	 * 
	 */
	@Test
	public void testNestedDifferentXmls() {
		String xml1="<?xml version=\"1.0\"?> <node> <element att1=\"a\" att2=\"b\"/><element>Test</element></node>";
		String xml2="<?xml version=\"1.0\"?> <node> <element>Test</element> <element att1=\"a\" att2=\"b\"/></node>";
		assertFalse(xmlComparator.isXmlEqual(xml1, xml2));
	}
}
