
Practical 10

Poker Hands
A poker deck contains 52 cards - each card has a suit which is one of clubs, diamonds, hearts, or spades (denoted C, D, H, S in the input data). Each card also has a value which is one of 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, ace (denoted 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A). For scoring purposes, the suits are unordered while the values are ordered as given above, with 2 being the lowest and ace the highest value.
A poker hand consists of 5 cards dealt from the deck. Poker hands are ranked by the following partial order from lowest to highest
High Card. Hands which do not fit any higher category are ranked by the value of their highest card. If the highest cards have the same value, the hands are ranked by the next highest, and so on.
Pair. 2 of the 5 cards in the hand have the same value. Hands which both contain a pair are ranked by the value of the cards forming the pair. If these values are the same, the hands are ranked by the values of the cards not forming the pair, in decreasing order.
Two Pairs. The hand contains 2 different pairs. Hands which both contain 2 pairs are ranked by the value of their highest pair. Hands with the same highest pair are ranked by the value of their other pair. If these values are the same the hands are ranked by the value of the remaining card.
Three of a Kind. Three of the cards in the hand have the same value. Hands which both contain three of a kind are ranked by the value of the 3 cards.
Straight. Hand contains 5 cards with consecutive values. Hands which both contain a straight are ranked by their highest card.
Flush. Hand contains 5 cards of the same suit. Hands which are both flushes are ranked using the rules for High Card.
Full House. 3 cards of the same value, with the remaining 2 cards forming a pair. Ranked by the value of the 3 cards.
Four of a kind. 4 cards with the same value. Ranked by the value of the 4 cards.
Straight flush. 5 cards of the same suit with consecutive values. Ranked by the highest card in the hand.
Your job is to compare several pairs of poker hands and to indicate which, if either, has a higher rank.
Input
The input file contains several lines, each containing the designation of 10 cards: the first 5 cards are the hand for the player named ‘Black’ and the next 5 cards are the hand for the player named ‘White’.
Output
For each line of input, print a line containing one of:
Black wins.
White wins. Tie.
Universidad de Valladolid OJ: 10315 – Poker Hands	2/2
 
Sample Input
2H 3D 5S 9C KD 2C 3H 4S 8C AH
2H 4S 4C 2D 4H 2S 8S AS QS 3S
2H 3D 5S 9C KD 2C 3H 4S 8C KH
2H 3D 5S 9C KD 2D 3H 5C 9S KH
Sample Output
White wins.
Black wins.
Black wins. 
Tie.



Program:















import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

class Main {
	
	static class Card implements Comparable<Card> {
		int value;
		char suit;
		
		public int compareTo(Card c) {
			if (this.value!=c.value) {
				return this.value-c.value;
			}
			return this.suit-c.suit;
		}
	}
	
	public static void main (String[]args) throws IOException  {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String s;
		
		HashMap<Character,Integer> charToValue=new HashMap<>();
		for (int i=1;i<10;i++) {
			charToValue.put((char)(i+'0'), i);
		}
		charToValue.put('T',10);
		charToValue.put('J',11);
		charToValue.put('Q',12);
		charToValue.put('K',13);
		charToValue.put('A',14);
		
		while ((s=br.readLine())!=null) {
			StringTokenizer st=new StringTokenizer(s);
			Card [] blackCards=new Card[5];
			Card [] whiteCards=new Card[5];
			
			for (int i=0;i<blackCards.length;i++) {
				String cStr=st.nextToken();
				Card c=new Card();
				c.value=charToValue.get(cStr.charAt(0));
				c.suit=cStr.charAt(1);
				blackCards[i]=c;
			}
			for (int i=0;i<whiteCards.length;i++) {
				String cStr=st.nextToken();
				Card c=new Card();
				c.value=charToValue.get(cStr.charAt(0));
				c.suit=cStr.charAt(1);
				whiteCards[i]=c;
			}
			
			//Sort for easier execution
			Arrays.sort(blackCards);
			Arrays.sort(whiteCards);
			
			int [] blackScore=getScore(blackCards);
			int [] whiteScore=getScore(whiteCards);
			String text="";
			if (blackScore[0]>whiteScore[0]) {
				text="Black wins.";
			} else if (whiteScore[0]>blackScore[0]) {
				text="White wins.";
			} else {
				if (blackScore[1]>whiteScore[1]) {
					text="Black wins.";
				} else if (whiteScore[1]>blackScore[1]) {
					text="White wins.";
				} else {
					int v=-1;
					//Flush, High Cards
					if (blackScore[0]==6 || blackScore[0]==1) {
						v=highCard(blackCards,whiteCards);
					} else if (blackScore[0]==3 || blackScore[0]==2) {
						v=comparePair(blackCards,whiteCards);
					}
					if (v==0) {
						text="Black wins.";
					} else if (v==1) {
						text="White wins.";
					} else {
						text="Tie.";
					}
				}
			}
			
			System.out.println(text);
		}
	}
	
	public static int [] getScore (Card [] c) {
		int [] rank=new int [2];
		
		int straightV=straight(c);
		int flushV=flush(c);
		
		int [] calcDupValueV=calculateDuplicateValue(c);
		
		if (straightV!=-1 && flushV!=-1) {
			rank[0]=9;
			rank[1]=straightV;
			return rank;
		}
		
		int fourOfAKindV = fourOfAKind(calcDupValueV);
		if (fourOfAKindV!=-1) {
			rank[0]=8;
			rank[1]=fourOfAKindV;
			return rank;
		}
		
		//full house
		int tripleV = triple(calcDupValueV);
		int pairsCountV = pairCount(calcDupValueV);
		if (tripleV!=-1 && pairsCountV==1) {
			rank[0]=7;
			rank[1]=tripleV;
			return rank;
		}
		
		if (flushV!=-1) {
			rank[0]=6;
			rank[1]=flushV;
			return rank;
		}
		
		if (straightV!=-1) {
			rank[0]=5;
			rank[1]=straightV;
			return rank;
		}

		if (tripleV!=-1 && pairsCountV==0) {
			rank[0]=4;
			rank[1]=tripleV;
			return rank;
		}
		

		if (pairsCountV==2) {
			rank[0]=3;
			rank[1]=pairMax(calcDupValueV);
			return rank;
		}
		
		if (pairsCountV==1) {
			rank[0]=2;
			rank[1]=pairMax(calcDupValueV);
			return rank;
		}
		
		rank[0]=1;
		rank[1]=c[c.length-1].value;
		return rank;
	}
	
	public static int [] calculateDuplicateValue(Card [] c) {
		int [] v=new int [15];
		for (int i=0;i<c.length;i++) {
			v[c[i].value]++;
		}
		return v;
	}
	
	public static int fourOfAKind(int [] v) {
		for (int i=0;i<v.length;i++) {
			if (v[i]==4) {
				return i;
			}
		}
		return -1;
	}
	
	public static int flush (Card [] c) {
		for (int i=1;i<c.length;i++) {
			if (c[i].suit!=c[i-1].suit) {
				return -1;
			}
		}
		return c[c.length-1].value;
	}
	
	public static int straight(Card [] c) {
		for (int i=1;i<c.length;i++) {
			if (c[i].value-c[i-1].value!=1) {
				return -1;
			}
		}
		return c[c.length-1].value;
	}
	
	public static int triple(int [] valuesCount) {
		for (int i=0;i<valuesCount.length;i++) {
			if (valuesCount[i]==3) {
				return i;
			}
		}
		return -1;
	}
	
	public static int pairCount(int [] valuesCount) {
		int pairsCount=0;
		for (int i=0;i<valuesCount.length;i++) {
			if (valuesCount[i]==2) {
				pairsCount++;
			}
		}
		return pairsCount;
	}
	
	public static int pairMax(int [] valuesCount) {
		int pairMax=-1;
		for (int i=0;i<valuesCount.length;i++) {
			if (valuesCount[i]==2) {
				pairMax=Math.max(pairMax, i);
			}
		}
		return pairMax;
	}
	
	public static int highCard(Card [] c1, Card [] c2) {
		for (int i=c1.length-1;i>=0;i--) {
			if (c1[i].value>c2[i].value) {
				return 0;
			} else if (c1[i].value<c2[i].value) {
				return 1;
			}
		}
		return -1;
	}
	
	public static int comparePair (Card [] c1, Card [] c2) {
		int [] calcDupValueV1=calculateDuplicateValue(c1);
		int [] calcDupValueV2=calculateDuplicateValue(c2);
		
		int [] c1PV=new int [2];
		int c1PVCount=0;
		for (int i=2;i<calcDupValueV1.length;i++) {
			if (calcDupValueV1[i]==2) {
				c1PV[c1PVCount++]=i;
			}
		}
		
		int [] c2PV=new int [2];
		int c2PVCount=0;
		for (int i=2;i<calcDupValueV1.length;i++) {
			if (calcDupValueV2[i]==2) {
				c2PV[c2PVCount++]=i;
			}
		}
		
		for (int i=c1PVCount-1;i>=0;i--) {
			if (c2PV[i]>c1PV[i]) {
				return 1;
			} else if (c2PV[i]<c1PV[i]) {
				return 0;
			}
		}
		
		//Still not found yet. Compare the remaining card...
		Card [] c1x=new Card [5-c1PVCount*2];
		int c1xCount=0;
		
		for (int i=0;i<5;i++) {
			if (calcDupValueV1[c1[i].value]==1) {
				c1x[c1xCount++]=c1[i];
			}
		}
		
		Card [] c2x=new Card [5-c2PVCount*2];
		int c2xCount=0;
		for (int i=0;i<5;i++) {
			if (calcDupValueV2[c2[i].value]==1) {
				c2x[c2xCount++]=c2[i];
			}
		}
		
		return highCard(c1x,c2x);
	}
}









Input:
2H 3D 5S 9C KD 2C 3H 4S 8C AH
2H 4S 4C 2D 4H 2S 8S AS QS 3S
2H 3D 5S 9C KD 2C 3H 4S 8C KH
2H 3D 5S 9C KD 2D 3H 5C 9S KH
Output:
White wins.
Black wins.
Black wins. 
Tie.

