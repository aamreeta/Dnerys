/**
 * Author: Amrita Gautam
 * email: aamreeta@gmail.com
 */
import java.io.IOException;
import org.custommonkey.xmlunit.Diff;
import org.custommonkey.xmlunit.XMLUnit;
import org.xml.sax.SAXException;

public class XmlComparator {
	/**
	 * Compares two xmls 
	 * @param xml1 
	 * @param xml2
	 * @return      Returns true if the xmls are identical or similar else returns false
	 *              
	 */

public boolean isXmlEqual(String xml1,String xml2){
		
		XMLUnit.setIgnoreWhitespace(true);
		try {
			Diff diff=XMLUnit.compareXML(xml1, xml2);
			if(diff.identical() || diff.similar())
				return true;
		} catch (SAXException | IOException e) {
			
			e.printStackTrace();
		}
		return false;
		
	}
 

}
