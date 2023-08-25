import java.util.Scanner;

public class JavaFactory {

    public static void main(String[] args) {
        // Scanner in = new Scanner(System.in);
        // String comida = in.nextLine();

        FoodFactory foodFactory = new FoodFactory();

        Food food = foodFactory.getFood("pizza");
        food.getType();

    }
}

class FoodFactory {

    public Food getFood(String tipoComida) {
        if ("pizza".equals(tipoComida)) {
            return new Pizza();
        } else if ("cake".equals(tipoComida)) {
            return new Cake();
        }

        return null;
    }
}

interface Food {
    void getType();
}

class Pizza implements Food {

    @Override
    public void getType() {
        System.out.println("The factory returned class Pizza \nSomeone ordered a Fast Food!");
    }
}

class Cake implements Food {

    @Override
    public void getType() {
        System.out.println("The factory returned class Cake \nSomeone ordered a Dessert!");
    }
}