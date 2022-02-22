import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;


public class MainM {
//
//    //    throws IOException необходимо чтобы не вылетало исключение
//    public static void main(String[] args) throws IOException {
//
//        File file = new File("D:\\foto");
//
//        String[] listfiles = file.list();
//        for (String files : listfiles) {
//
////            создание объекта класса File
//            File files1 = new File("D:\\foto\\" + files);
//
////            условие проверки, что файл является файлом, а не каталогом
////            чтоб исключить создание каталога на основе уже имеющегося каталога
//            if (files1.isFile()) {
//
////                получаем дату - год из названия файла
//                String year = files.substring(0, 4);
////                получаем дату - месяц из названия файла
//                String month = files.substring(4, 6);
//                String yearMonth = year + "." + month;
//
////                создаем новый каталог в зависимости от имеющихся файлов (по дате и месяцу)
//                File file1 = new File("D:\\foto\\" + yearMonth);
//                boolean isCreated = file1.mkdir();
//
////                формирование пути к файлу (от куда берем файл)
//                Path path1 = Path.of("D:\\foto\\", files);
////                формирование нового пути куда переносим
//                Path path2 = Path.of("D:\\foto\\", yearMonth, files);
//
////                метод перемещения файла из первой директории (path1) во вторую (path2)
//                Files.move(path1, path2);
//
//            }
//        }
//    }
}


// 2570 файлов перемещено за менее, чем 1 секунду (15,7 Гб инфы)