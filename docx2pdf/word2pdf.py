import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
 
import com.aspose.words.Document;
import com.aspose.words.License;
import com.aspose.words.SaveFormat;
 
public class Word2PdfUtil {
 
    private static boolean getLicense() {
        boolean result = false;
        try {
            InputStream is = Word2PdfUtil.class.getClassLoader().getResourceAsStream("license.xml"); // license.xml应放在..\WebRoot\WEB-INF\classes路径下
            License aposeLic = new License();
            aposeLic.setLicense(is);
            result = true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return result;
    }
 
    /**
     * @param wordPath
     *            需要被转换的word全路径带文件名
     * @param pdfPath
     *            转换之后pdf的全路径带文件名
     */
    public static void doc2pdf(String wordPath, String pdfPath) {
        if (!getLicense()) { // 验证License 若不验证则转化出的pdf文档会有水印产生
            return;
        }
        try {
            long old = System.currentTimeMillis();
            File file = new File(pdfPath); // 新建一个pdf文档
            FileOutputStream os = new FileOutputStream(file);
            Document doc = new Document(wordPath); // Address是将要被转化的word文档
            doc.save(os, SaveFormat.PDF);// 全面支持DOC, DOCX, OOXML, RTF HTML, OpenDocument, PDF, EPUB,
                                         // XPS, SWF 相互转换
            long now = System.currentTimeMillis();
            os.close();
            System.out.println("共耗时：" + ((now - old) / 1000.0) + "秒"); // 转化用时
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
 
    public static void main(String[] args) {
 
        doc2pdf("D:\\98_App\python\00_develop\docx2pdf\TestDocument.doc", "D:\\98_App\python\00_develop\docx2pdf\test.pdf");
    }
}