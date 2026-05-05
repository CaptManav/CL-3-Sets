import java.rmi.Naming;

public class Server {
    public static void main(String[] args) {
        try {
            StringConcat obj = new StringConcatImpl();

            Naming.rebind("rmi://localhost:1099/concatService", obj);

            System.out.println("Server ready...");
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}