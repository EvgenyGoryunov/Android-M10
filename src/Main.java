import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        main_finaly();
    }


    static String get_file_extension(File path_to_files) {
//        функция получения расширения файла (без точки) на вход подаем объект класс File
//        в виде пути к папке с файлами для анализа берет первый файл

        System.out.println("вход в функцию: get_file_extension");

        String[] list_files1 = path_to_files.list();
//        получили список файлов директории

        for (String name_file : list_files1) {
            String[] devided_file_name = name_file.split("\\.");
            String file_extension = devided_file_name[devided_file_name.length - 1];
            if (Objects.equals(file_extension, "py")) {
                System.out.println("return py;");
                return "py";

            } else if (Objects.equals(file_extension, "java")) {
                System.out.println("return java;");
                return "java";
            }
        }
        return null;
    }


    static String add_or_del(File path_to_files, String file_extension) throws IOException {
//        функция поиска в файле спец символов экранирования, выдает значения

        System.out.println("вход в функцию: add_or_del");

        String[] list_files = path_to_files.list();
//        создаем пустой массив (список) String[] list_files, в который при помощи метода list()
//        помещаем список файлов данной директории

        System.out.println("1111проверка");
        for (String name_file : list_files) {

//            File files1 = new File(".\\qqq\\" + name_file);
            File files1 = new File(".\\" + name_file);
//            формируем полный путь до файла, то есть директория + имя файла, чтоб в дальнейшем обращаться
//            к самому файлу, к конечному объекту
            System.out.println(files1);
            System.out.println("2222проверка");
            System.out.println("значение file_extension расширения на вход: " + file_extension);
            if (files1.isFile()) {
                System.out.println("3333проверка");
//                проверка на то, что данный объект является файлом, а не директорией (каталог)

                Scanner one_file = new Scanner(new FileInputStream(files1));
//                грузим в поток файл (в переменную one_file)
                System.out.println("4444проверка");
                while (one_file.hasNextLine()) {
                    System.out.println("5555проверка");
//                    циклом проверяем, есть ли в нашем файле символы экранирования
                    String string_from_file = one_file.nextLine();
                    if (file_extension.equals("java")) {
                        System.out.println("javajavajavajava");
                        if (string_from_file.contains("//") & string_from_file.contains("System.out.print")) {
                            return "del";
//                            если в одной строчке одновременно есть символы "//" и строка печати (out.print)
                        } else if (!string_from_file.contains("//") & string_from_file.contains("System.out.print")) {
                            return "add";
                        }
                    } else if (file_extension.equals("py")) {
                        System.out.println("pypypypypypy");

                        if (string_from_file.contains("# print")) {
//                            System.out.println("return del");
                            return "del";
//                            если в одной строчке одновременно есть символы "#" и строка печати (print)
                        } else if (string_from_file.contains("  print")) {
//                            System.out.println("return add");
                            return "add";
                        }
                    }
                }
                one_file.close();
//                закрываем поток
            }
        }
        return null;
    }


    static void main_finaly() throws IOException {
        System.out.println("вход в функцию: main_finaly");

        File path_to_files = new File(".\\");
//        File path_to_files = new File(".\\qqq\\");
//        path_to_files - переменная, в которой содержиться путь к директории, где лежат файлы
//        (если точка - значит текущая директория, где находятся файлы (либо файл)


        String extension = get_file_extension(path_to_files);
//        вызываем функцию, получаем от нее расширение файлов, либо джава либо питон

        String add_or_del_char = add_or_del(path_to_files, extension);
//        вызываем функцию, получаем значение Строка, удалять символ экранирования, либо добавлять
        System.out.println("значение add_or_del_char на входе в main_finaly(): " + add_or_del_char);

        String[] list_files = path_to_files.list();
//        создаем пустой массив (список) String[] list_files, в который при помощи метода list()
//        помещаем список файлов данной директории

        for (String name_file : list_files) {
            System.out.println("name_file - " + name_file);
//            создаем цикл, в котором перебираем каждый файл из списка (имена файлов)

//            File files1 = new File(".\\qqq\\" + name_file);
            File files1 = new File(".\\" + name_file);
//            формируем полный путь до файла, то есть директория + имя файла

            if (files1.isFile() & add_or_del_char != null) {
//                условие, что файл является файлом и значение от функции определения дел или адд символ

                ArrayList<String> array_for_string = new ArrayList<String>();
//                создаем пустой массив для помещения в него уже измененных строк (экранированные или наоборот)

                Scanner one_file1 = new Scanner(new FileInputStream(files1));
//                запускаем поток входных данных из файла

                while (one_file1.hasNextLine()) {
//                цикл с условием, что мы пройдемся по всем строчкам файла

                    String string_from_file = one_file1.nextLine();
//                     вызывая метод nextLine() мы загружаем следующую строчку в переменную string_from_file

                    System.out.println("--------------------------------------------");
                    System.out.println("изначальная строка: " + string_from_file);

                    if (Objects.equals(extension, "py") & Objects.equals(add_or_del_char, "add")) {
//                        условия отработки строк, финальная подготовка
                        String modified_string = string_from_file.replaceAll(" {2}print", "# print");
                        array_for_string.add(modified_string);
                        System.out.println("111готовая строка: " + modified_string);
                    } else if (Objects.equals(extension, "py") & Objects.equals(add_or_del_char, "del")) {
                        String modified_string = string_from_file.replaceAll("# print", "  print");
                        array_for_string.add(modified_string);
                        System.out.println("222готовая строка: " + modified_string);
                    } else if (Objects.equals(extension, "java") & Objects.equals(add_or_del_char, "del")) {
                        if (string_from_file.contains("//") & string_from_file.contains("System.out.print")) {
                            String modified_string = string_from_file.replaceAll("//", "");
                            array_for_string.add(modified_string);
                            System.out.println("333готовая строка: " + modified_string);
                        } else {
                            array_for_string.add(string_from_file);
                            System.out.println("333-111готовая строка: " + string_from_file);
                        }
                    } else if (Objects.equals(extension, "java") & Objects.equals(add_or_del_char, "add")) {
                        if (!string_from_file.contains("//") & string_from_file.contains("System.out.print")) {
                            String modified_string = "//" + string_from_file;
                            array_for_string.add(modified_string);
                            System.out.println("444готовая строка: " + modified_string);
                        } else {
                            array_for_string.add(string_from_file);
                            System.out.println("444-111готовая строка: " + string_from_file);
                        }
                    }
                }
                System.out.println("готовый массив array_for_string: " + array_for_string);

                one_file1.close();
//                обязательно нужно закрыть поток, иначе файл не сможет удалиться, т.к будет занят
                if (files1.isFile()) {
                    PrintWriter writer = new PrintWriter(files1);
//                так как функция удаления не срабатывает (поток не могу закрыть), перезапишем файл пустыми строками
                    writer.print("");
                    writer.close();
                    System.out.println("функция PrintWriter очистиля исходный файл");
                }


//                FileWriter write_to_finish_file = new FileWriter(".\\qqq\\" + name_file, true);

                if (files1.isFile()) {
                    FileWriter write_to_finish_file = new FileWriter(".\\" + name_file, true);

                    for (String mod_srt_from_array : array_for_string) {
//                        вписываем в файл новые, измененные строки и сохраняем по очереди каждую строчку
                        write_to_finish_file.write(mod_srt_from_array + "\n");
                        write_to_finish_file.flush();
                    }
                }


                System.out.println("функция FileWriter записала массив array_for_string в файл");
            }
        }
    }
}











