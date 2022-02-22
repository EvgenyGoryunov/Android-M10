import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.text.SimpleDateFormat;
import java.util.*;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        add_simbol();
    }

    private static void add_simbol() throws IOException {


        File path_to_files = new File(".\\qqq");
//        path_to_files - переменная, в которой содержиться путь к директории, где лежат файлы
//        (если точка - значит текущая директория, где находятся файлы (либо файл)

        String[] list_files = path_to_files.list();
//        создаем пустой массив (список) String[] list_files, в который при помощи метода list()
//        помещаем список файлов данной директории


        for (String name_file : list_files) {
            System.out.println("name_file - " + name_file);
//            создаем цикл, в котором перебираем каждый файл из списка (имена файлов)

//            System.out.println(files);


            File files1 = new File(".\\qqq\\" + name_file);
//            формируем полный путь до файла, то есть директория + имя файла, чтоб в дальнейшем обращаться
//            к самому файлу, к конечному объекту
//            System.out.println(files1);

            if (files1.isFile()) {
//                проверка на то, что данный объект является файлом, а не директорией (каталог), может быть так
//                что содержится подкаталог, который программа видит как объект и рабоате с ним, хотя нам нужны файлы
//                System.out.println(files1);

                Scanner one_file = new Scanner(new FileInputStream(files1));
//                считываем файл переменную one_file

                ArrayList<String> array_for_string = new ArrayList<String>();
//                создаем пустой массив для помещения в него строк из файла

                while (one_file.hasNextLine()) {
//                цикл с условием, что мы пройдемся по всем строчкам файла

                    String string_from_file = one_file.nextLine();
//                     вызывая метод nextLine() мы загружаем следующую строчку в переменную string_from_file

//                    String modified_string = string_from_file.replaceAll("# print", " print");
                    String modified_string = string_from_file.replaceAll(" {2}print", "# print");

                    array_for_string.add(modified_string);

                    System.out.println("--------------------------------------------");
                    System.out.println("изначальная строка: " + string_from_file);
                    System.out.println("готовая строка: " + modified_string);
                }

                System.out.println("готовый массив " + array_for_string);

                one_file.close();
//                обязательно нужно закрыть поток, иначе файл не сможет удалиться, т.к будет открыт поток

                boolean isDeleted = files1.delete();
//                удаляем изначальный файл для того, чтоб создать новый с таким же именем
                System.out.println("файл удален - " + isDeleted);

                FileWriter write_to_finish_file = new FileWriter(".\\qqq\\" + name_file, true);

                for (String mod_srt_from_array : array_for_string) {
                    write_to_finish_file.write(mod_srt_from_array + "\n");
                    write_to_finish_file.flush();

                }
            }
        }
    }
}










