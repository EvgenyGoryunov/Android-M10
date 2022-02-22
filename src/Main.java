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
//        MainMM.randMessages();
        add_simbol();
    }

    private static void add_simbol() throws IOException {


        Path path = Path.of(".\\cod1\\Test.txt");
        List<String> list = Files.readAllLines(path);


        String value = null;
        for (String str : list)
//            System.out.println(str);
            value = str.replaceAll("1", "111");
            System.out.println(value);



//
////        получить файл
////        пройтись по каждой строчке
////        произвести замену
////        сохранить файл
//
////
//        String file_name = "Test.txt";
//
//        File file = new File(".\\cod1", file_name);
////        поместили в переменную file файл Test.txt
//
//        Scanner msg = new Scanner(new FileInputStream(file));
////        считываем переменную file, то есть файл Test.txt
//
//        String s = msg.nextLine();
////        в переменную s мы помещаем по одной строчки при каждом вызове метода nextLine()
//
//        while (msg.hasNextLine()) {
////            цикл с условием, что мы пройдемся по всем строчкам файла дословно, что пока есть строчки, мы будем его выполнять
//
//            s = msg.nextLine();
////            вызывая это строчку, мы каждый раз загружаем новую, следующую строчку в переменную S
//
//            String value = s.replaceAll("2", "22222");
////            переменная value равно измененной правильной строчке
//
////            записать обратно в файл измененную строчку, либо создать новый файл тогда уж
////
//
//
//
//            FileWriter messWrite = new FileWriter("Test1.txt", true);
//            messWrite.write(value + "\n");
//            messWrite.flush();
//
//
//            System.out.println(s);
//            System.out.println(value);


        }


//            System.out.println(msg.next());


//        System.out.println(s);
//        s = msg.nextLine();
//        System.out.println(s);
//        s = msg.nextLine();
//        System.out.println(s);

        //        System.out.println(msg);

//        while (msg.hasNextLine()) {
//            System.out.println(msg.next());
//        }
//
//        msg.close();

//
//        FileWriter messWrite = new FileWriter(".code_ready/Test.txt", true);
//        messWrite.write(" ШУТКА" + "\n");
//        messWrite.flush();


//        File file = new File(".\\cod_ready", "Test.txt");


//        File file = new File(".\\cod_ready", "Test.txt");
//        File file = new File(".\\cod_ready", "Test.txt");
//
//        File file1 = new File("C:\\Test");
//        String[] files1 = file.list();

//        File file = new File(".\\cod_ready\\Test.txt" );
//        System.out.println(file.getText());


//        System.out.println("qqqq");
//        System.out.println(file.getName());
//        System.out.println(file.getPath());
//        System.out.println(file1.list());

//        File directory = new File("C:\\Test");
//        File file = new File(directory, "Test.txt");
//        System.out.println(file.getName());
    }













