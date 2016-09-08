#include <SFML/Graphics.hpp>
#include <time.h>
#include <sstream>
using namespace sf;

const int M = 20;
const int N = 10;

int field[M][N] = {0};

struct Point {int x,y;} 
	a[4], b[4];

int figures[7][4] = {
	1,3,5,7, // I
	2,4,5,7, // Z
	3,5,4,6, // S
	3,5,4,7, // T
	2,3,5,7, // L
	3,5,7,6, // J
	2,3,4,5, // O
};

bool check(){
   for (int i = 0; i < 4; i++)
	  if (a[i].x < 0 || a[i].x >= N || a[i]. y>= M) 
		  return 0;
      else if (field[a[i].y][a[i].x]) 
		  return 0;

   return 1;
};


int main(){
    srand(time(0));	 

	RenderWindow window(VideoMode(1000, 628), "Tetris!");

    Texture t1,t2,t3;
	t1.loadFromFile("images/tiles.png");
	t2.loadFromFile("images/dragon.jpg");
	t3.loadFromFile("images/frame.png");

	Sprite s(t1), background(t2), frame(t3);
	frame.setPosition(70,89);
	
	Font font;
	font.loadFromFile("fonts/Rurintania.ttf");

    int dx = 0; 
	bool rotate = 0; 
	int colorNum = 1;
	float timer = 0;
	float delay = 1; 
	int playerScore = 0;

	bool pause = false;
	bool gameover = false;

	Clock clock;

    while (window.isOpen()){
		float time = clock.getElapsedTime().asSeconds();
		clock.restart();
		
        Event e;
        while (window.pollEvent(e)){
            if (e.type == Event::Closed)
                window.close();

			if (e.type == Event::KeyPressed)
			  if (e.key.code == Keyboard::Up) 
				  rotate = true;
			  else if (e.key.code == Keyboard::Left) 
				  dx = -1;
			  else if (e.key.code == Keyboard::Right) 
				  dx = 1;
			  else if (e.key.code == Keyboard::Space)
				  pause = !pause;
		}
		
		if (!pause && !gameover)
			timer += time;
		else {
			dx = 0; 
			rotate = 0;
		}

		if (Keyboard::isKeyPressed(Keyboard::Down)) 
			delay = 0.05;

		//// <- Move -> ///
		for (int i = 0; i < 4; i++){ 
		      b[i] = a[i]; 
				a[i].x += dx; 
		}
        
		if (!check()) 
			for (int i = 0; i < 4; i++) 
				a[i] = b[i];
			
		//////Rotate//////
		if (rotate){
			Point p = a[1]; //center of rotation
			for (int i = 0; i < 4; i++){
				int x = a[i].y - p.y;
				int y = a[i].x - p.x;
				a[i].x = p.x - x;
				a[i].y = p.y + y;
	 		}
   			if (!check()) 
				for (int i=0;i<4;i++) 
					a[i]=b[i];
		}	

		///////Tick//////
		if (timer > delay){
		    for (int i = 0; i < 4; i++){ 
				b[i] = a[i]; 
				a[i].y += 1; 
			}
				
			if (!check()){
			for (int i=0;i<4;i++) 
				field[b[i].y][b[i].x] = colorNum;

			colorNum = 1 + rand() % 7;
			int n = rand() % 7;
			for (int i = 0; i < 4; i++){
			    a[i].x = figures[n][i] % 2;
			    a[i].y = figures[n][i] / 2;
			 }
			}
	  		timer = 0;
		}

		///////check lines//////////
		int k = M - 1;
		for (int i = M - 1; i > 0; i--){
			int count = 0;
			for (int j = 0; j < N;j++){
			    if (field[i][j]) count++;
			    field[k][j]=field[i][j];
			}
			if (count<N) 
				k--;
			else 
				playerScore += 10;
		}	

	    dx = 0; 
		rotate = 0; 
		delay = 1;

	    /////////draw//////////
	    window.clear(Color::White);	
	    window.draw(background);
			  
		for (int i = 0; i < M; i++)
			for (int j = 0; j < N; j++){
				if (field[i][j] == 0) continue;
					s.setTextureRect(IntRect(field[i][j]*18,0,18,18));
					s.setPosition(j*18,i*18);
					s.move(100,120); //offset
					window.draw(s);
			}

		for (int i = 0; i < 4; i++){
			s.setTextureRect(IntRect(colorNum*18,0,18,18));
			s.setPosition(a[i].x*18,a[i].y*18);
			s.move(100,120); //offset
			if (field[a[i].y][a[i].x])
				gameover = true;
			else window.draw(s);
		}

		window.draw(frame);

		Text score("", font, 30);
		score.setColor(Color::White);
		score.setPosition(80, 500);
		std::ostringstream playerScoreString;
		playerScoreString << playerScore;
		score.setString("Your scrore: " + playerScoreString.str());
		window.draw(score);

		if (gameover){
				Text text("Game Over", font, 40);
				text.setColor(Color(244,244,244));
				text.setPosition(75, 30);
				text.setStyle(Text::Bold | Text::Italic);
				window.draw(text);
		}

 		window.display();
	}

    return 0;
}