label = ['a1','a2','a3','b0','b1','b2','b3','b4','c1',
                'c2','c3','c4','d1','d2','d3','d4','e1','e2','e3','e4','f1','f2','f3']
def list_to_dict(board):
    XO=[]
    for i in board:
        if i==1:
            XO.append('O')
        elif i==2:
            XO.append('X')
        else:
            XO.append(())
    newdict=dict(zip(label, XO))
    #print(newdict)
    return(newdict)


def dict_to_list(dict1):
    listn=list(dict1.values())
    listn.insert(3, listn.pop(0))
    for i in range(len(listn)):
        if listn[i] =='X':
            listn[i]=2
        elif listn[i]=='O':
            listn[i]=1
        else:
            listn[i]=0
    return(listn)

def phasecheck(board): #checks which phase the game is in
    if board.count(1)>=15:
        return(1)
    else:
        return(0)
    
def adjspace(pos):
    special=0
    if pos==3:
        x=[1,5, 9, 13]
    elif pos==0:
        x=[ 1, 4,]
    elif pos==1:
        x=[-1, 1, 4]
    elif pos==21:
        x=[-1, 1, -4]
    elif pos in [2, 7]:
        x=[-1, 4]
    elif pos in [11, 15]:
        #c4 & d4 [-4 -1 4]
        x=[-1, 4, -4]
    elif pos in [19, 22]:
        #e4 & f3 [-4 -1]
        x=[-1, -4]
    elif pos==20:
        #f1 [1 -4]
        x=[1, -4]
    elif pos in [8,12,16]:
        x=[1, 4, -4]
        special=1
    else:
        x=[-1, 1, 4, -4]
    return(x, special)

def future_states(board):
    state_f=[]
    for i in range(len(board)):
        boardcopy=board.copy()
        if phasecheck(board)==0 and board[i]==0:
            boardcopy[i]=1
            #print(boardcopy)
            state_f.append(boardcopy)
        elif phasecheck(board)==1 and board[i]==1: #only adjacent spots
            moves, sp=adjspace(i)
#             print(sp)
            for move in moves:
                if boardcopy[i+move]==0:
#                     print('\n')
                    boardcopy=board.copy()
                    boardcopy[i+move]=1
                    boardcopy[i]=0
#                     print('move:',label[i],'moved to:',label[i+move])
                    state_f.append(boardcopy)
#                     dispboard(boardcopy)
                else:
                    pass
            if sp==1 and board[3]==0:#going up doesnt work
                boardcopy=board.copy()
                boardcopy[3]=1
                boardcopy[i]=0
                state_f.append(boardcopy)
            else:
                pass    
    #print(len(state_f))
    return(state_f)



testcase={'b0': 'X', 'a1': (), 'a2': (), 'a3': (), 'b1': (), 'b2': (), 'b3': (), 'b4': (), 'c1': 'X', 'c2': (), 'c3': 'O', 'c4': (), 'd1': (), 'd2': (), 'd3': (), 'd4': 'O', 'e1': 'X', 'e2': (), 'e3': (), 'e4': (), 'f1': (), 'f2': (), 'f3': ()}
testlist=dict_to_list(testcase) #changes the dict to list format 
future_states(testlist) #iterates through the list and generates future moves

