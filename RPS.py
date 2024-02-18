# Rock Paper Scissors in Teachscript 

var names = ["Rock", "Paper", "Scissors"];

function computerMove() {
	var z = Integer(3 * math.random());
	assert(z == 0 or z == 1 or z == 2); 
	return z;
}


function playerMove() {
	setEventHandler("canvas.keydown", function(event) { 
		var k = event.key;
		if(k.size() == 1 and k>="1" and k<="3") then quitEventMode(Integer(k)-1);
	});
	return enterEventMode(); 
}


function computeWinner(player, computer) {
	if player == computer then return "Kein Gewinner";
	else if player == 0 and computer == 2 then return "Player";
	else if player == 1 and computer == 0 then return "Player"; 
	else if player == 2 and computer == 1 then return "Player";
	else return "Computer"; 
} 


function execute() {
	print("Drücke eine Taste von 0-2 um eine Auswahl zu tätigen:");
	print("0 = Rock");
	print("1 = Paper");
	print("2 = Scissors");
	var playerChoice = playerMove();
	var computerChoice = computerMove();
	print("");
	print("Ergebnis: ");
	print("Player - " + names[playerChoice]); 
	print("Computer - " + names[computerChoice]); 
	print("");
	print("Gewinner: " + computeWinner(playerChoice, computerChoice));
}

execute(); 


	
	
	
