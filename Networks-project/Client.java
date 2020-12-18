import java.io.*;
import java.net.*;
import java.util.*;
 
/**
 *  implement a UDP client program.
 *
 */

public class Client {
    private static final int MAX_TIMEOUT = 1000;	// milliseconds
    public static void main(String[] args) throws Exception {

      Random random = new Random();
      double loss_rate = 0.455535;
      int lossCounter = 0;
      int ServerPort = 9999;
      int count = 0;

      try {

          InetAddress address = InetAddress.getLocalHost();
          DatagramSocket socket = new DatagramSocket(3333);
          byte[] message = ("Hi").getBytes();
          while (count<10) {
              Date now = new Date();
              long msSend = now.getTime();
              DatagramPacket request = new DatagramPacket(message, message.length, address, ServerPort);
              count++;
              
              // random loss of packets
              if (random.nextFloat() <= loss_rate) {
                lossCounter++;
                System.out.println("packet loss");
                continue;
              }

              socket.send(request);
              try {
                // Set up the timeout 1000 ms = 1 sec
                socket.setSoTimeout(MAX_TIMEOUT);
                // Set up an UPD packet for recieving
                DatagramPacket response = new DatagramPacket(new byte[1024], 1024);
                // Try to receive the response from the ping
                socket.receive(response);
                // If the response is received, the code will continue here, otherwise it will continue in the catch
                
                // timestamp for when we received the packet
                now = new Date();
                long msReceived = now.getTime();
                // Print the packet and the RTT
                printData(response, msReceived - msSend);
              } catch (IOException e) {
                // Print which packet has timed out
                System.out.println("Request Timeout for packet no. " + count);}      
          }
      System.out.println("");    
      System.out.println("Ping statistics for: "+address.getHostAddress());
      System.out.println("    packets: sent = "+10+"   Received = "+(10-lossCounter)+
      "   Lost = "+lossCounter + " ("+(lossCounter*100)/10 +"% loss)");  
      
      socket.close();

      } catch (SocketTimeoutException ex) {
          System.out.println("Timeout error: " + ex.getMessage());
          ex.printStackTrace();
      } catch (IOException ex) {
          System.out.println("Client error: " + ex.getMessage());
          ex.printStackTrace();} 
    }
    
    private static void printData(DatagramPacket request, long delayTime) throws Exception
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
         "Replay from " + 
         request.getAddress().getHostAddress() + 
         ": " +
         new String(line.trim()) + "   RTT: " + delayTime +" ms"  );
   }
}