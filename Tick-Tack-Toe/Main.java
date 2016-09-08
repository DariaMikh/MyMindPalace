
public class Main {
	public static void main(String[] args){

        XO game = new XO();
        boolean end = false;

        while(true){
            game.printField();
            game.makeAMoveX();            
            end = game.checkWinner();
            if (end == true)
                break;
            System.out.println("\n");
            
            game.printField();
            game.makeAMoveO();
            end = game.checkWinner();
            if (end == true)
                break;
            System.out.println("\n");
        }       
    }
}
