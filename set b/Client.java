import java.rmi.Naming;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try {
            StringConcat stub = (StringConcat) Naming.lookup("rmi://localhost:1099/concatService");

            Scanner sc = new Scanner(System.in);

            System.out.print("Enter first string: ");
            String s1 = sc.nextLine();

            System.out.print("Enter second string: ");
            String s2 = sc.nextLine();

            String result = stub.concat(s1, s2);

            System.out.println("Concatenated String: " + result);

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}