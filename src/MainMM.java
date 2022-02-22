import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.*;


public class MainMM {

    public static void main(String[] args) throws IOException {

//        randMessages();

    }


    public static void randMessages() throws IOException {

//        создаем объект класса Файл, в который помещаем директорию
        File file = new File(".\\text");

//        создаем массив listfiles, в который помещаем список файлов, содержащихся в директории ".\\text"
        String[] listfiles = file.list();

//        цикл для формирования сообщений на 7 дней (на неделю вперед)
        for (int z = 0; z < 7; z++) {

//            цикл для формирования правильно сообщения
            for (int i = 0; i < 2; i++) {

//                условие, при котором первой строчкой формируется пунктирная линия разделитель + дата
                if (i == 0) {

//                    создаем объект класса календарь
                    Calendar calendar = new GregorianCalendar();
//                    добавляет нашей дате при каждом цикле одно значение, чтоб было смещение по датам
                    calendar.add(Calendar.DATE, z);
//                    получить текущее значение даты и времени
                    Date dateNow = calendar.getTime();

//                    формирование правильно вывода даты (число, месяц, год)
                    SimpleDateFormat formatter = new SimpleDateFormat("EEEE (dd-MMMM-YYYY)");
                    String dateMessage = formatter.format(dateNow);

//                    записать в файл Test.txt сообщение в виде: 1-пунктирная линия, 2-дата
                    FileWriter qwe = new FileWriter("./Test.txt", true);
//                    вписываем линию
                    qwe.write("\n------------------------------------------------------------------------------------" + "\n");
//                    вписываем дату
                    qwe.write("дата: " + dateMessage + "\n");
                    qwe.flush();

//               условие, при котором прописывается фраза шутка дня
                } else if (i == 1) {

                    FileWriter messWrite = new FileWriter("./Test.txt", true);
                    messWrite.write(" ШУТКА" + "\n");
                    messWrite.flush();

                    int j = 0;

//                    циклом выводим все фразы, по одной из каждого документа
                    for (String files : listfiles) {

                        if (j <= 1) {

                            File pathFiles = new File(".\\text\\" + files);

//                            создаем поток инфы из файла
                            Scanner message = new Scanner(new FileInputStream(pathFiles));
//                            создаем список, в который в дальшейшем поместим наши строчки с файлов
                            ArrayList<String> messList = new ArrayList<String>();

//                            через цикл while проходимся по каждой строчке сверху вниз и добавляем в наш список
//                            каждую строчку
                            while (message.hasNextLine()) {
                                messList.add(message.nextLine());
                            }

//                            создаем объект класс рандом, для выбора из нашего списка случайной фразы
                            Random randomMess = new Random();
                            String rrr = messList.get(randomMess.nextInt(messList.size()));

//                            выбранную случайную фразу прописываем в наш текстовый файл
                            FileWriter qwe1 = new FileWriter("./Test.txt", true);
//                            формат вывода сообщения в файл
                            messWrite.write((j + 1) + ". " + rrr + "\n");
                            messWrite.flush();

//                            условие, при котором вписывается фраза "мотивашки"
                            if (j == 1) {
                                messWrite.write(" МОТИВАЦИЯ " + "\n");
                                messWrite.flush();
                            }

                            j += 1;

//                            условие написания мотивашек (2шт)
                        } else if (j > 1) {

                            File pathFiles = new File(".\\text\\" + files);

                            Scanner jokeOfComp = new Scanner(new FileInputStream(pathFiles));
                            ArrayList<String> messageMes = new ArrayList<String>();

                            while (jokeOfComp.hasNextLine()) {
                                messageMes.add(jokeOfComp.nextLine());
                            }

                            Random randomMotiv = new Random();
                            String mesMes = messageMes.get(randomMotiv.nextInt(messageMes.size()));

                            messWrite.write((j - 1) + ". " + mesMes + "\n");
                            messWrite.flush();

                            j += 1;

                        }
                    }
                }
            }
        }
    }
}

