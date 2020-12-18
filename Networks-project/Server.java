import java.io.*;
import java.net.*;

 
/**
 *  implement a UDP server program.
 * 
 */
public class Server {
    public static void main(String[] args) throws Exception {
      int count = 5;
      try{
      int port = 9999;
      DatagramSocket socket = new DatagramSocket(port);
      System.out.println("server waiting...");

      while (count<10) {
        // Create a datagram packet to hold incomming UDP packet.
        DatagramPacket request = new DatagramPacket(new byte[1024], 1024);

        // Block until the host receives a UDP packet.
        socket.receive(request);
       
        // Print the recieved data.
        printData(request);

        // Send reply.
        InetAddress clientHost = request.getAddress();
        int clientPort = request.getPort();
        byte[] buf = ("Hello").getBytes();

        DatagramPacket reply = new DatagramPacket(buf, buf.length, clientHost, clientPort);
        count++;
        socket.send(reply); }

      } catch (SocketTimeoutException ex) {
        System.out.println("Timeout error: " + ex.getMessage());
        ex.printStackTrace();
      }   catch (IOException ex) {
        System.out.println("Client error: " + ex.getMessage());
        ex.printStackTrace();}  
        
       
  } 
   
  private static void printData(DatagramPacket request) throws Exception
   {
      // Obtain references to the packet's array of bytes.
      byte[] buf = request.getData();

      // Wrap the bytes in a byte array input stream,
      // so that you can read the data as a stream of bytes.
      ByteArrayInputStream bais = new ByteArrayInputStream(buf);

      // Wrap the byte array output stream in an input stream reader,
      // so you can read the data as a stream of characters.
      InputStreamReader isr = new InputStreamReader(bais);

      // Wrap the input stream reader in a bufferred reader,
      // so you can read the character data a line at a time.
      // (A line is a sequence of chars terminated by any combination of \r and \n.)
      BufferedReader br = new BufferedReader(isr);

      // The message data is contained in a single line, so read this line.
      String line = br.readLine();

      // Print host address and data received from it.
      System.out.println(
         "Received from " +
         request.getAddress().getHostAddress() +
         ": " +
         new String(line.trim()) );
   } 
}