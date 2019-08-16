//  Conlon

import java.io.*;
import java.util.*;

public class CityList2
{
  public static void main( String[] args ) throws Exception 
  {
    Scanner file = new Scanner( new File("DATACityList.txt") );
    Scanner fileIn = new Scanner( new File("DATAShortList.txt") );
    ArrayList<String> city = new ArrayList<String>();
    String w = "", list = "";
    while( file.hasNext() ) // list of all cities
    {
      w = file.nextLine(); // data could have blank space
      city.add(w);      
    }
    for ( int i = 0; i < 5; i++ ) 
    {
      list = fileIn.next(); // each set of suggestions, String of UpperCase letters
      for ( int x=0; x<list.length(); x++ ) 
      {
        String letter = list.substring(x, x+1);
        for ( String y : city ) // match each letter to a city
        {
          if( y.startsWith(letter) )
          {
            System.out.print(y + " ");
            break;
          } // more efficient to break once we find it
        }
      }
      System.out.println();
    } // end 5 data for
  } // end main
}