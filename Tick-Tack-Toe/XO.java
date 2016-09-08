import java.util.Scanner;

 class XO {
	private char field[];
    private int movesCounter;
    private int cellNumber;

    public XO(){
    	field = new char[9];
        for (int i = 0; i < 9; i++){
            field[i] = (char)(i + 49);
        }
        movesCounter = 0;
        cellNumber = 0;
    }
    
    public void printField(){
        for (int i = 0, j = 0; j < 3; i += 3, j++){
        	System.out.print("     |     |     \n");
        	System.out.print("  " + field[i] + "  |  " + field[i+1] + "  |  " + field[i+2] + "  \n");
        	System.out.print("_____|_____|_____\n");
        }
        System.out.println();
    }
    
    public void makeAMoveX(){
        System.out.print("\nPlayer 1 make a move.\n");
        boolean correctEnter = false;
        while(!correctEnter){
            cellNumber = new Scanner(System.in).nextInt();;
            if (cellNumber > 0 && cellNumber < 10){
                if ((int)field[cellNumber-1] - 48 == cellNumber){
                    field[cellNumber-1] = 'X';
                    movesCounter++;
                    correctEnter = true;
                }
                else
                	System.out.print("This cell is occupied.\n");
            }
            else
            	System.out.print("Wrong number.\n");
        }
    }
    
    public void makeAMoveO(){
        System.out.print("\nPlayer 2 make a move.\n");
        boolean correctEnter = false;
        while(!correctEnter){
            cellNumber = new Scanner(System.in).nextInt();;
            if (cellNumber > 0 && cellNumber < 10){
                if ((int)field[cellNumber-1] - 48 == cellNumber){
                    field[cellNumber-1] = 'O';
                    movesCounter++;
                    correctEnter = true;
                }
                else
                	System.out.print("This cell is occupied.\n");
            }
            else
            	System.out.print("Wrong number.\n");
        }
    }
    
    public boolean checkWinner(){
        if (movesCounter > 4){
            //По горизонтали
            for (int i = 0, j = 0; j < 3; i += 3, j++){
                if(field[i] == field[i+1] && field[i] == field[i+2]){
                    printWinner(i);
                    return true;
                }
            }
            //По вертикали
            for (int i = 0, j = 0; j < 3; i++, j++){
                if(field[i] == field[i+3] && field[i] == field[i+6]){
                    printWinner(i);
                    return true;
                }
            }
            //По диагонали
            if((field[0] == field[4] && field[0] == field[8]) || (field[2] == field[4] && field[2] == field[6])){
                printWinner(4);
                return true;
            }
        }
        if (movesCounter == 9){
        	System.out.print("Drawn game.\n");
            return true;
        }
        return false;
    }
    
    public void printWinner(int i){
        if (field[i] == 'X')
        	System.out.print("\nPlayer 1 is winner!\n\n");
        else if (field[i] == 'O')
        	System.out.print("\nPlayer 2 is winner!\n\n");
        else
        	System.out.print("\nError.\n");
    }
}


