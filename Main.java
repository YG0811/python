import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Запит користувача на введення кількості днів
        System.out.print("Введіть кількість днів: ");
        int numberOfDays = scanner.nextInt();

        // Створення масиву для збереження температур
        double[] temperatures = new double[numberOfDays];

        // Введення температур користувачем
        for (int i = 0; i < numberOfDays; i++) {
            System.out.print("Введіть температуру для дня " + (i + 1) + ": ");
            temperatures[i] = scanner.nextDouble();
        }

        // Закриваємо сканер
        scanner.close();

        // Обчислення середньої температури
        double sum = 0;
        for (double temp : temperatures) {
            sum += temp;
        }
        double averageTemperature = sum / numberOfDays;

        // Підрахунок кількості днів, коли температура була вищою за середню
        int aboveAverageCount = 0;
        for (double temp : temperatures) {
            if (temp > averageTemperature) {
                aboveAverageCount++;
            }
        }

        // Сортування масиву для знаходження найхолодших і найгарячих днів
        java.util.Arrays.sort(temperatures);

        // Виведення результатів
        System.out.println("Середня температура за всі дні: " + averageTemperature);
        System.out.println("Кількість днів, коли температура була вищою за середню: " + aboveAverageCount);

        if (numberOfDays >= 2) {
            System.out.println("Два найхолодші дні: " + temperatures[0] + "°C і " + temperatures[1] + "°C");
            System.out.println("Два найгарячіші дні: " + temperatures[numberOfDays - 1] + "°C і " + temperatures[numberOfDays - 2] + "°C");
            String[] deck = new String[52];
            String[] deckReversed = new String[52];

// Заповнення масиву deck числами від 1 до 52
            for (int i = 0; i < 52; i++) {
                deck[i] = String.valueOf(i + 1);
            }

// Заповнення масиву deckReversed числами від 52 до 1 в оберненому порядку
            for (int i = 0; i < 52; i++) {
                deckReversed[i] = String.valueOf(52 - i);
            }

        }
    }
}

