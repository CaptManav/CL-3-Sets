import java.rmi.Remote;
import java.rmi.RemoteException;

public interface StringConcat extends Remote {
    String concat(String s1, String s2) throws RemoteException;
}