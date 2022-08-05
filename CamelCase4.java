import java.io.*;
import java.util.*;

//This program performs some action on each new line given in this format:
//C;C;example word
//
//the two actions (functions) are splitting and combining, this is given in 
//the first input parameter, the second input parameter stands for the type 
//of name being dealt with - method, class or variable name
//splitting converts a name from camel case to space seperated words
//combining converts space seperated words into camel case method, class or 
//variable names
//
//these are examples of proper method, class and variable names:
// methodName() ClassName variableName


public class Solution {
    
    static Scanner sc = new Scanner(System.in);

    char[] split(char[] input){
        
        char[] strOut1;
        String strOut="";
        char[] subArray;
        String strAdd;
        
        int ind=0;
        int flag=1;
        
        for(int i=0;i < input.length;i++){
            
            if(i==(input.length - 1)){
                subArray = Arrays.copyOfRange(input, ind, i+1);
                strAdd = new String(subArray);
                strAdd = strAdd.toLowerCase();
                if(flag==1){
                    strOut = strOut.concat(strAdd);
                }else{
                    strOut = strOut.concat(" ");
                    strOut = strOut.concat(strAdd);
                }
            }
            if(input[i]<91){
                
                if(i==0){
                    continue;
                }
                
                subArray = Arrays.copyOfRange(input, ind, i);
                strAdd = new String(subArray);
                strAdd = strAdd.toLowerCase();
                
                if(flag==1){
                    strOut = strOut.concat(strAdd);
                    flag++;
                }else{
                    strOut = strOut.concat(" ");
                    strOut = strOut.concat(strAdd);
                } 
                
                ind = i;
            }
        }
        
        strOut1 = strOut.toCharArray();
        
        return strOut1;
    }
    
    char[] combine(char[] input){
        
        char[] strOut1;
        String strOut="";
        char[] subArray;
        String strAdd;

        int ind=0;
        int flag=1;
        
        for(int i=0;i < input.length;i++){
            if(i==(input.length - 1)){
                subArray = Arrays.copyOfRange(input, ind, i+1);
                if(flag==1){
                    strAdd = new String(subArray);
                    strOut = strOut.concat(strAdd);
                }else{
                    subArray[0] = Character.toUpperCase(subArray[0]);
                    strAdd = new String(subArray);
                    strOut = strOut.concat(strAdd);
                }
            }
            if(input[i]==' '){
                if(i==0){
                    continue;
                }
                
                subArray = Arrays.copyOfRange(input, ind, i);
                
                if(flag==1){
                    strAdd = new String(subArray);
                    strOut = strOut.concat(strAdd);
                    flag++;
                }else{
                    subArray[0] = Character.toUpperCase(subArray[0]);
                    strAdd = new String(subArray);
                    strOut = strOut.concat(strAdd);
                } 
                
                ind = i+1;
            }
        }
        
        strOut1 = strOut.toCharArray();
        
        //char[] strOut1 = {'c','o','m','b','i','n','e'};
        
        return strOut1;   
    }

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        
        Solution obj = new Solution();
        
        while(sc.hasNextLine()){
            
            String strIn = sc.nextLine();
            
            char c1,c2;
            
            char[] strIn1;
            char[] strOut1;
            char[] subArray;
            String strOut;
            
            c1 = strIn.charAt(0);
            c2 = strIn.charAt(2);
            
            strIn1= strIn.toCharArray();
            strIn1 = Arrays.copyOfRange(strIn1, 4, strIn.length());
            
            if(c1 == 'S' || c1=='C'){
                if(c1 == 'S'){
                    if(c2 == 'M'){
                        subArray = Arrays.copyOfRange(strIn1, 0, strIn.length() - 2 - 4);
                    }else{
                        subArray = strIn1;
                    }
                    
                    strOut1 = obj.split(subArray);
                    strOut = new String(strOut1);
                    
                    System.out.println(strOut);
                }
                if(c1 == 'C'){
                    
                    strOut1 = obj.combine(strIn1);
                    
                    if(c2 == 'M'){
                        strOut = new String(strOut1);
                        strOut = strOut.concat("()");
                        System.out.println(strOut);
                    }else if (c2 == 'C'){
                        strOut1[0] = Character.toUpperCase(strOut1[0]);
                        strOut = new String(strOut1);
                        System.out.println(strOut);
                    }else if(c2 == 'V'){
                        strOut = new String(strOut1);
                        System.out.println(strOut);   
                    }else{
                        System.out.println("INVALID");
                    }
                }
            } else {
                System.out.println("INVALID");
            }
        }
    }
}
