import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;


// для JAR-файл, способного работать из любой папки (относительные пути)
public class MainPort {

//    public static void main(String[] args) throws IOException {
//
//        File file = new File(".");
//
//        String[] listfiles = file.list();
//        for (String files : listfiles) {
//
//            File files1 = new File(".\\" + files);
//
//            if (files1.isFile()) {
//
//                String year = files.substring(0, 4);
//                String month = files.substring(4, 6);
//                String yearMonth = year + "." + month;
//
//                File file1 = new File(".\\" + yearMonth);
//                boolean isCreated = file1.mkdir();
//
//                Path path1 = Path.of(".\\", files);
//                Path path2 = Path.of(".\\", yearMonth, files);
//
//                Files.move(path1, path2);
//
//            }
//        }
//    }
}