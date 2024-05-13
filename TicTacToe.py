import pygame


COLOR={'black':[000,000,000],
      'white':[225,225,225],
      'green':[000,225,000],
      'red':[225,000,000],
      'gray':[150,150,150],
      'yellow':[255,255,0],
      }

pygame.init()



class things:
    def __init__(self):
        things.WINDOW=pygame.display.set_mode([800,800])
        things.OFF_X=True
        things.OFF_O=True
        things.ON_O=True
        things.ON_X=True
        things.decide_O=True
        things.decide_X=False
        things.BORDER_LINETOP1=pygame.Rect(389,200,6,364)
        things.BORDER_LINETOP2=pygame.Rect(389+119,200,6,364)
        things.BORDER_LINESIDE1=pygame.Rect(270,319,363,6)
        things.BORDER_LINESIDE2=pygame.Rect(270,319+119,363,6)
        things.WINNER_BOX=(341,271,210,156)
        things.font=pygame.font.SysFont(None,28)
        things.font_2=pygame.font.SysFont(None,40)
        things.img_player1=things.font.render('player_1',True,COLOR['black'])
        things.img_player2=things.font.render('player_2',True,COLOR['black'])
        things.img_O=things.font.render('O',True,COLOR['black'])
        things.img_X=things.font.render('X',True,COLOR['black'])
        things.img=things.font.render('reset',True,COLOR['black'])
        things.img_exit=things.font.render('exit',True,COLOR['black'])
        things.WINNER_WORD=things.font_2.render('WINNER!',True,COLOR['black'])
        things.box_board=pygame.Rect(270,200,363,364)
        things.reset_button=pygame.Rect(85,220,90,80) #reset_button
        things.exit_button=pygame.Rect(122-36,390-40,88,75)
        things.location=[]
        things.location_X_even=[]
        things.location_X_odd=[]
        things.display_O_board=[]
        things.display_X_board_even=[]
        things.display_X_board_odd=[]
        things.GRAB_call_loc=[]
        things.GRAB_call_evens=[]
        things.GRAB_call_odds=[]
        things.violate_O_steps=[]
        things.violate_X_steps=[]
        things.merge_VOS_AND_VXS=[]
        things.WINNING_NUMBERS=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        things.LOTTER_X_ADD=[]
        things.ANSWER_WINNER_O=False
        things.ANSWER_WINNER_X=False
        for i in range(19):
            things.location.append(i)
        for ev in range(18):
            if ev%2==0:
                things.location_X_even.append(ev)
        for od in range(18):
            if od%2!=0:
                things.location_X_odd.append(od)

        things.clock=pygame.time.Clock()

if __name__=='__main__':
    things()



class data_board:
    def __init__(self):
        data_board.smallbox_rect=[]
        data_board.X_Y=[]
        data_board.DATA_LEAN_RIGHT=[]
        data_board.DATA_LEAN_LEFT=[]



class boxing:
    def __init__(self,num_x,num_y,size,add_box):
        boxing.switch=True
        self.num_x=num_x
        self.num_y=num_y
        boxing.num=None
        self.size=size
        self.add_box=add_box
        for i in range(self.add_box):
            boxing.SQUARES=pygame.Rect(self.num_x,self.num_y,self.size,self.size)
            pygame.draw.rect(things.WINDOW,COLOR['black'],boxing.SQUARES,3)
            boxing.num=self.num_x,self.num_y
            if boxing.switch:
                data_board.X_Y.append(boxing.num)
                data_board.smallbox_rect.append(boxing.SQUARES)

                if len(data_board.smallbox_rect)==self.add_box:
                    boxing.switch=False

            self.num_x+=119



def draw_circle(number):
    for i in range(8):
        centerX_Y=pygame.Rect(data_board.X_Y[number],(125,125))
        center=centerX_Y.x+65,centerX_Y.y+65
        return center



def X_LEAN_RIGHT(x1,x2,x3,x4):

    for looping in range(3):
        #pygame.draw.line(things.WINDOW,COLOR['yellow'],(x1,x2),(x3,x4),4)
        EVEN0=x1,x2
        ODD1=x3,x4
        data_board.DATA_LEAN_RIGHT.append((EVEN0))
        data_board.DATA_LEAN_RIGHT.append((ODD1))
        x1+=121;x2+=2;x3+=123



def X_LEAN_LEFT(x1,x2,x3,x4):
    for looping in range(3):
        #pygame.draw.line(things.WINDOW,COLOR['red'],(x1,x2),(x3,x4),4)
        EVEN0=x1,x2
        ODD1=x3,x4
        data_board.DATA_LEAN_LEFT.append((EVEN0))
        data_board.DATA_LEAN_LEFT.append((ODD1))
        x1+=121;x2-=3;x3+=124



def STOP_REPEATER_LIST(GRAB_CALL,LISTS,REMOVE_LAST):
    zero=0

    if GRAB_CALL in LISTS:
        if 0==zero:
            zero-=1

        else:
            zero=0
            LISTS[zero]=GRAB_CALL
    else:
        LISTS.append(GRAB_CALL.removesuffix(REMOVE_LAST))
        zero+=1


def checkgoing_right(GRAB_call_loc):
    if GRAB_call_loc not in things.GRAB_call_evens:
        things.violate_O_steps.append(GRAB_call_loc)
        return GRAB_call_loc



def checkgoing_left(GRAB_call_evens):
    Y=len(GRAB_call_evens)-1
    if GRAB_call_evens not in things.GRAB_call_loc:
        things.violate_X_steps.append(GRAB_call_evens)
        return GRAB_call_evens


    Y-=1


def check(search_a_word,inside_list):
    if search_a_word in inside_list:
        return False

    else:
        return True


def WHOS_TURN():
    if len(things.violate_O_steps)>=len(things.violate_X_steps):
       things.decide_X=False


    if len(things.violate_X_steps)>=len(things.violate_O_steps):
        things.decide_O=True


    else:
        things.decide_X=True;things.decide_O=False


def SEARCH_ENGINE(LEN_inbox,total_LEN,search_FOR,ALL_STEPS_L,WEB_LIST):
    NEXT_NUMBER=[]#'start:'
    ONEUP=0
    RESTNUM=0
    STORAGE=[]
    MATCHING=[]
    STORAGE.append(search_FOR)
    look_again=-len(ALL_STEPS_L)


    for loop_out in range(len(STORAGE)):
        if loop_out%4==0:
            for LOOP_IN in range(total_LEN):
                if STORAGE[loop_out] in WEB_LIST[LOOP_IN]:
                    MATCHING.append(WEB_LIST[LOOP_IN])



    if len(ALL_STEPS_L)!=0:
        #print('THE POSSIBLITIES:',MATCHING)
        #print('STEPS:',ALL_STEPS_L)
        BOX_1=[];BOX_2=[];BOX_3=[];BOX_4=[]
        Y_OR_N_NEXT=[]
        for loop_oneuper in MATCHING:
            for characters_loop in loop_oneuper:
                if characters_loop in ALL_STEPS_L:
                    Y_OR_N_NEXT.append('yes')


                elif characters_loop not in ALL_STEPS_L:
                    Y_OR_N_NEXT.append('none')


    for number in range(len(Y_OR_N_NEXT)):
        if number<=2:
            BOX_1.append(Y_OR_N_NEXT[number])
        elif number>=2 and number<=5:
            BOX_2.append(Y_OR_N_NEXT[number])

        elif number>=5 and number<=8:
            BOX_3.append(Y_OR_N_NEXT[number])

        elif number>=8 and number<=12:
            BOX_4.append(Y_OR_N_NEXT[number])



    if BOX_1.count('yes')==3 or BOX_2.count('yes')==3 or BOX_3.count('yes')==3 and len(BOX_4)==0:
        return True



class step_board:
    def __init__(self):


        step_board.pressing_evens={
                 'zero_X_L':things.location_X_even[0],
                 'one_X_L':things.location_X_even[1],
                 'two_X_L':things.location_X_even[2],
                 'three_X_L':things.location_X_even[3],
                 'four_X_L':things.location_X_even[4],
                 'five_X_L':things.location_X_even[5],
                 'six_X_L':things.location_X_even[6],
                 'seven_X_L':things.location_X_even[7],
                 'eight_X_L':things.location_X_even[8],
                 }


        step_board.call_evens=['zero_X_L','one_X_L','two_X_L','three_X_L','four_X_L','five_X_L','six_X_L','seven_X_L','eight_X_L']


        step_board.pressing_odds={
                 'zero_X_R':things.location_X_odd[0],
                 'one_X_R':things.location_X_odd[1],
                 'two_X_R':things.location_X_odd[2],
                 'three_X_R':things.location_X_odd[3],
                 'four_X_R':things.location_X_odd[4],
                 'five_X_R':things.location_X_odd[5],
                 'six_X_R':things.location_X_odd[6],
                 'seven_X_R':things.location_X_odd[7],
                 'eight_X_R':things.location_X_odd[8],
                 }


        step_board.call_odds=['zero_X_R','one_X_R','two_X_R','three_X_R','four_X_R','five_X_R','six_X_R','seven_X_R','eight_X_R']


        step_board.pressing={
                 'zero_O':things.location[0],
                 'one_O':things.location[1],
                 'two_O':things.location[2],
                 'three_O':things.location[3],
                 'four_O':things.location[4],
                 'five_O':things.location[5],
                 'six_O':things.location[6],
                 'seven_O':things.location[7],
                 'eight_O':things.location[8],
                 }


        step_board.call_loc=['zero_O','one_O','two_O','three_O','four_O','five_O','six_O','seven_O','eight_O']

if __name__=='__main__':
    step_board()



def controls():

    if event.type==pygame.MOUSEBUTTONDOWN:
        if event.button==1:
            if  things.decide_O:
                for i in range(9):#9
                    things.ON_O=True;things.OFF_O=True
                    if things.BORDER_LINETOP1.colliderect((event.pos),(6,364)) or things.BORDER_LINETOP2.colliderect((event.pos),(6,364)) or things.BORDER_LINESIDE1.colliderect((event.pos),(363,6)) or things.BORDER_LINESIDE2.colliderect((event.pos),(363,6)):
                        things.OFF_O=False
                    if data_board.smallbox_rect[i].collidepoint(event.pos):
                        things.ON_O=True
                        things.ON_O=((things.ON_O and things.OFF_O)and(check(step_board.call_loc[i].removesuffix('_O'),things.merge_VOS_AND_VXS) and not things.decide_X))
                        if things.ON_O:
                            STOP_REPEATER_LIST(step_board.call_loc[i],things.GRAB_call_loc,'_O')
                            things.display_O_board.append(step_board.pressing[step_board.call_loc[i]])
                            things.ANSWER_WINNER_O=SEARCH_ENGINE(2,8,i,things.display_O_board,things.WINNING_NUMBERS)
                            GRAB=checkgoing_right(things.GRAB_call_loc[-1])
                            things.merge_VOS_AND_VXS.append(GRAB)




            if things.decide_X:
                for I in range(9):#9
                    things.ON_X=True;things.OFF_X=True
                    if things.BORDER_LINETOP1.colliderect((event.pos),(6,364)) or things.BORDER_LINETOP2.colliderect((event.pos),(6,364)) or things.BORDER_LINESIDE1.colliderect((event.pos),(363,6)) or things.BORDER_LINESIDE2.colliderect((event.pos),(363,6)):
                        things.OFF_X=False
                    if data_board.smallbox_rect[I].collidepoint(event.pos):
                        things.ON_X=True
                        things.ON_X=((things.ON_X and things.OFF_X)and(check(step_board.call_loc[I].removesuffix('_O'),things.merge_VOS_AND_VXS) and not things.decide_O))
                        if things.ON_X:
                            STOP_REPEATER_LIST(step_board.call_evens[I],things.GRAB_call_evens,'_X_L')
                            STOP_REPEATER_LIST(step_board.call_odds[I],things.GRAB_call_odds,'_X_R')
                            things.display_X_board_even.append(step_board.pressing_evens[step_board.call_evens[I]])
                            things.display_X_board_odd.append(step_board.pressing_odds[step_board.call_odds[I]])
                            things.LOTTER_X_ADD.append(I)
                            things.ANSWER_WINNER_X=SEARCH_ENGINE(2,8,I,things.LOTTER_X_ADD,things.WINNING_NUMBERS)
                            GRAB=checkgoing_left(things.GRAB_call_evens[-1])
                            things.merge_VOS_AND_VXS.append(GRAB)



            WHOS_TURN()



        if event.button==1:
            if things.reset_button.collidepoint(event.pos):
                if len(things.display_O_board)>=0:
                    things.display_O_board.clear();things.LOTTER_X_ADD.clear()
                    things.display_X_board_even.clear();things.display_X_board_odd.clear()
                    things.GRAB_call_loc.clear()
                    things.GRAB_call_evens.clear();things.GRAB_call_odds.clear()
                    things.violate_O_steps.clear()
                    things.violate_X_steps.clear()
                    things.merge_VOS_AND_VXS.clear();things.decide_X=False;things.decide_O=True
                    things.ANSWER_WINNER_O=False;things.ANSWER_WINNER_X=False



        if event.button==1:
            if things.exit_button.collidepoint(event.pos):
                exit()



RUNNER=True
while RUNNER:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            RUNNER=False


        controls()


    things.WINDOW.fill(COLOR['white'])
    pygame.draw.rect(things.WINDOW,COLOR['gray'],things.box_board)


    if __name__=='__main__':
        data_board()
    boxing(270,200,125,3)
    boxing(270,319,125,3)
    boxing(270,438,125,3)


    X_LEAN_LEFT(283,215,372,304)
    X_LEAN_LEFT(283,337,372,426)
    X_LEAN_LEFT(283,459,372,548)
    #pygame.draw.line(things.WINDOW,COLOR['red'],data_board.DATA_LEAN_LEFT[0],data_board.DATA_LEAN_LEFT[1],4)



    X_LEAN_RIGHT(381,208,285,304)
    X_LEAN_RIGHT(381,334,286,429)
    X_LEAN_RIGHT(381,460,287,554)
    #pygame.draw.line(things.WINDOW,COLOR['yellow'],data_board.DATA_LEAN_RIGHT[0],data_board.DATA_LEAN_RIGHT[1],4)



    if len(things.display_O_board)>0:
        for i in range(len(things.display_O_board)):
            pygame.draw.circle(things.WINDOW,COLOR['yellow'],draw_circle(things.display_O_board[i]),40,3)



    if len(things.display_X_board_even)>0:
        for all in range(len(things.display_X_board_even)):
            pygame.draw.line(things.WINDOW,COLOR['black'],data_board.DATA_LEAN_RIGHT[things.display_X_board_even[all]],data_board.DATA_LEAN_RIGHT[things.display_X_board_odd[all]],4)



    if len(things.display_X_board_odd)>0:
        for all in range(len(things.display_X_board_odd)):
            pygame.draw.line(things.WINDOW,COLOR['black'],data_board.DATA_LEAN_LEFT[things.display_X_board_even[all]],data_board.DATA_LEAN_LEFT[things.display_X_board_odd[all]],4)


    #example
    '''even=4;odds=5
    pygame.draw.line(things.WINDOW,COLOR['red'],data_board.DATA_LEAN_LEFT[even],data_board.DATA_LEAN_LEFT[odds],4)
    pygame.draw.line(things.WINDOW,COLOR['yellow'],data_board.DATA_LEAN_RIGHT[even],data_board.DATA_LEAN_RIGHT[odds],4)#'''



    pygame.draw.circle(things.WINDOW,COLOR['green'],(130,260),50)
    pygame.draw.circle(things.WINDOW,COLOR['red'],(130,387),50)
    pygame.draw.rect(things.WINDOW,COLOR['black'],things.box_board,2)
    things.WINDOW.blit(things.img,(104,250))
    things.WINDOW.blit(things.img_exit,(100+10,380))
    things.WINDOW.blit(things.img_player1,(290-19,144))
    things.WINDOW.blit(things.img_player2,(584-30,144))


    if things.decide_O:
        hightlight_red=(269,134,83,61)
    if things.decide_X:
        hightlight_red=(552,134,86,61)
    pygame.draw.rect(things.WINDOW,COLOR['red'],hightlight_red,2)
    things.WINDOW.blit(things.img_O,(308,174))
    things.WINDOW.blit(things.img_X,(592,176))


    if len(things.merge_VOS_AND_VXS)==9:#9
        things.decide_O=False;things.decide_X=False


    def display_winner_surface(img_player,TURN_OFF_ANSWER):
        things.decide_O=False;things.decide_X=False
        pygame.draw.rect(things.WINDOW,COLOR['white'],things.WINNER_BOX)
        pygame.draw.rect(things.WINDOW,COLOR['red'],things.WINNER_BOX,5)
        things.WINDOW.blit(things.WINNER_WORD,(385,282))
        things.WINDOW.blit(img_player,(410,357))
        TURN_OFF_ANSWER=False


    if things.ANSWER_WINNER_O:
        display_winner_surface(things.img_player1,things.ANSWER_WINNER_X)
    if things.ANSWER_WINNER_X:
        display_winner_surface(things.img_player2,things.ANSWER_WINNER_O)


    pygame.display.update()
    things.clock.tick(60)



if __name__=='__main__':
    pygame.quit()
