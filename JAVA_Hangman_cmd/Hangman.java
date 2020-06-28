import java.util.*;
import java.lang.System;
import java.io.*;

class Hangman{

    public static String getWord(){
        double randomNum = Math.random();
        int index = (int)(Math.floor(randomNum*100));
        String[] common = {"the","of","and","ant","total","intelligent","island","you","that","bait","she","was","for","online","are","castor","with","his","they","open","at","be","this","have","from","valor","one","had","by","word","button","not","what","all","were","we","when","your","can","said","there","use","titan","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","goat","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"};
        return common[index];
    }

    public static void guess(String word){
        int guesses = 6;
        int wordLen = word.length();

        char[] wordArr = new char[wordLen];
        for(int i=0;i<wordLen;++i){
            wordArr[i] = word.charAt(i);
        }

        char[] guessed = new char[wordLen];
        for(int i=0;i<wordLen;++i){
            guessed[i] = '*';
        }

        System.out.println("Guess the word: ");
        for(char c:guessed) System.out.print(c);
        System.out.println();
        
        Scanner sc = new Scanner(System.in);
        while(guesses>0){
            System.out.println("Guess a character: ");
            char guessed_char = sc.nextLine().charAt(0);
            //Create guessed list check to prevent re entering of previously guessed char
            boolean isCorrect = false;
            for(int i=0;i<wordLen;++i){
                if(wordArr[i] == guessed_char){
                    isCorrect = true;
                    guessed[i] = guessed_char;
                }
            }
            if(isCorrect==false){
                System.out.println("Wrong guess");
                guesses--;
                System.out.println("Choices left: "+guesses);
            }
            boolean hasWon = true;
            for(char c:guessed){
                if(c=='*') hasWon = false;
            }
            if(!hasWon){
                for(char c:guessed) System.out.print(c);
                System.out.println("\n");
            }else{
                System.out.println("You won!");
                System.out.println("Word is "+word);
                return;
            }               
        }
        System.out.println("Word is "+word+". Better luck next time!");
        System.out.println("::: Game Over :::\n");
        return;
    }

    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        char choice = 'Y';
        while(choice=='Y'||choice=='y'){
            guess(getWord());
            System.out.println("Play again? (Y/N) ");
            choice=sc.next().charAt(0);
        }
        System.out.println("Thanks for playing Hangman.");
        sc.close();
    }
}