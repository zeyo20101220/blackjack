import random

# 카드 덱 생성 및 셔플
def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

# 카드 점수 계산 (A는 1 또는 11로 유연하게 계산)
def calculate_score(hand):
    score = 0
    aces = 0
    
    for card in hand:
        if card['rank'] in ['J', 'Q', 'K']:
            score += 10
        elif card['rank'] == 'A':
            score += 11
            aces += 1
        else:
            score += int(card['rank'])
            
    # 21점을 넘었을 때 A를 1로 변경
    while score > 21 and aces:
        score -= 10
        aces -= 1
        
    return score

# 카드 한 장 뽑기
def deal_card(deck, hand):
    hand.append(deck.pop())

# 카드 패 출력 포맷
def display_hand(player_name, hand, show_all=True):
    if show_all:
        cards_str = ", ".join([f"{c['suit']}{c['rank']}" for c in hand])
        print(f"{player_name}의 패: [{cards_str}] (점수: {calculate_score(hand)})")
    else:
        # 딜러의 첫 번째 카드만 공개할 때
        print(f"{player_name}의 패: [{hand[0]['suit']}{hand[0]['rank']}, ??]")

# 게임 메인 로직
def play_blackjack():
    print("♣♥♦♠ 블랙잭 게임을 시작합니다! ♠♦♥♣\n")
    deck = create_deck()
    
    player_hand = []
    dealer_hand = []
    
    # 처음 2장씩 나눠 갖기
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)
    deal_card(deck, player_hand)
    deal_card(deck, dealer_hand)
    
    # 초반 상태 보여주기
    display_hand("딜러", dealer_hand, show_all=False)
    display_hand("플레이어", player_hand)
    print("-" * 40)
    
    # 플레이어 턴
    while calculate_score(player_hand) < 21:
        choice = input("카드를 더 받으시겠습니까? (y/n): ").lower().strip()
        if choice == 'y':
            deal_card(deck, player_hand)
            display_hand("플레이어", player_hand)
            print("-" * 40)
        elif choice == 'n':
            break
        else:
            print("y 또는 n으로만 입력해 주세요.")
            
    player_score = calculate_score(player_hand)
    
    # 플레이어 버스트(21점 초과) 확인
    if player_score > 21:
        print("💥 21점을 초과(버스트)했습니다! 딜러 승리!")
        return

    # 딜러 턴 (딜러는 17점 이상이 될 때까지 무조건 카드를 받아야 함)
    print("\n[딜러의 턴]")
    display_hand("딜러", dealer_hand)
    
    while calculate_score(dealer_hand) < 17:
        print("딜러가 17점 미만이므로 카드를 한 장 더 받습니다.")
        deal_card(deck, dealer_hand)
        display_hand("딜러", dealer_hand)
        print("-" * 40)
        
    dealer_score = calculate_score(dealer_hand)
    
    # 최종 결과 판정
    print("\n🏆 [최종 결과]")
    display_hand("플레이어", player_hand)
    display_hand("딜러", dealer_hand)
    print()
    
    if dealer_score > 21:
        print("🥳 딜러 버스트! 플레이어 승리!")
    elif player_score > dealer_score:
        print("🥳 플레이어 승리!")
    elif player_score < dealer_score:
        print("🤖 딜러 승리!")
    else:
        print("🤝 무승부(푸시)입니다!")

# 게임 실행
if __name__ == "__main__":
    play_blackjack()
