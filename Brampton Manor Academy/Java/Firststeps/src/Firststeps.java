public class Firststeps {
    public static void main(String[] args) {
        yesloop();
        carloop();
        ifday();
        switchday();
    }



    public static void yesloop() {
        for (int i = 0; i <5;i++) {
            System.out.println("Yes");
        }
    }

    public static void carloop() {
        String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
        for (String el : cars) {
            System.out.println(el);
        }
    }

    public static void ifday() {
        int day = 4;
        if (day == 6) {
            System.out.println("Today is saturday");
        } else if (day == 7) {
            System.out.println("Today is Sunday");
        } else {
            System.out.println("looking forward to the weekend");
        }

    }

    public static void switchday() {
        int day = 6;
        switch(day) {
            case 6:
                System.out.println("Today is a saturday");
                break;
            case 7:
                System.out.println("Today is a sunday");
                break;
            default:
                System.out.println("Looking forward to the weekend");

        }
    }

    public static void Tryexcept() {
        int[] myNumber = {1, 2, 3};
        try {
            System.out.println(myNumber[10]);
        } catch ( "exception"){
            System.out.println("array index out of bounds")
        }
    }
    
}



