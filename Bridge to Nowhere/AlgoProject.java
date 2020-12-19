
package algoproject;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;
/**
 *
 * @author Anas Markhouss (438021838)
           Amr AL Gamal (438021843)
 */

public class AlgoProject {
    
    
    
        public static void LIS(int[] nums){
            // sizes array to keep track of longest LIS ending with current position
            
          String[] paths= new String[nums.length];
            int [] sizes= new int [nums.length];
            
            
            for(int i=0;i<nums.length;i++){
                sizes[i]=1;
                paths[i]=nums[i]+" ";
            
            }
            
           int maxLength=0;
           
           for(int i=0;i<nums.length;i++){
               for(int j=0;j<i;j++){
                   if(nums[i]>nums[j]&&sizes[i]<sizes[j]+1){
                       sizes[i]=sizes[j]+1;
                       paths[i]=paths[j]+nums[i]+" ";
                       
                       if(maxLength<sizes[i])
                           maxLength=sizes[i];
                   }
               }
           }
           
           
           for(int i=1; i<nums.length; i++){
               if(sizes[i]==maxLength){
                   System.out.println("LIS: "+paths[i]);
                   System.out.println("");
               break;
               }
           }
            System.out.println("Max number of bridges  = "+maxLength);
            
        }
        
        
        
     public static void main(String [] fff){
         
    Scanner in = new Scanner(System.in);
    int cityNum ;
    boolean Check = true;
    
    
        while(Check){
            try{
        System.out.println("Enter The number of cites 1 - 100");
        cityNum = in.nextInt();
        
        if(cityNum >= 1 && cityNum <=100 ){
        int[] n = new int[cityNum];
        
        int[] rand = Random(cityNum);
        
         for(int i = 0 ; i < n.length ; i++){
              n[i] = i+1;        
         }
         System.out.println(Arrays.toString(n));
         
         System.out.println("\n");
         
         System.out.print(Arrays.toString(rand));
         
         System.out.println("\n");
         
          LIS(rand);
          
          Check = false;
        }
        else{
            throw new Exception("Value is not vaild!");
        }
        
    }
        
        catch(Exception exception){
        System.out.println("Try again !");
        
         in.nextLine();
         
         Check = true;
    }
        }
       
        
     
     }
     
     public static int[] Random(int n){
     ArrayList<Integer> list = new ArrayList<>(n);
        for(int i = 1; i <= n; i++) {
            list.add(i);
        }
int st[]=new int [n];
int c=0;
        Random rand = new Random();
        while(list.size() > 0) {
            int index = rand.nextInt(list.size());
            st[c]=list.remove(index);
            c++;
        }
        
       return st;
     }
    }