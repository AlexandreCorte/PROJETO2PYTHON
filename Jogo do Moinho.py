def cria_posicao(c,l):
    """
    Esta funcao recebe duas strings, correspondentes a linha e a coluna
    do tabuleiro e retorna uma posicao de acordo com a representacao
    escolhida (tuple).
    Gera erro se a linha for diferente de 1,2,3 ou se a coluna for diferente
    de a,b,c.
    :param c: (string) primeiro parametro
    :param l: (string) segundo parametro
    :return: (tuple) posicao
    """
    if type(c)!=str or type(l)!=str or len(c)!=1 or len(l)!=1:
        raise ValueError('cria_posicao: argumentos invalidos')
    if c not in ('a', 'b', 'c') or l not in ('1', '2', '3'):
        raise ValueError('cria_posicao: argumentos invalidos')
    return (c,l)

def cria_copia_posicao(p):
    """
    Esta funcao recebe uma posicao e retorna uma copia da mesma.
    :param p: (tuple) posicao - unico parametro
    :return: (tuple) posicao copiada
    """
    return obter_pos_c(p),obter_pos_l(p)

def obter_pos_c(p):
    """
    Esta funcao recebe uma posicao e retorna a sua coluna (a,b,c).
    :param p: (tuple) posicao - unico parametro
    :return: (string) coluna
    """
    return p[0]

def obter_pos_l(p):
    """
    Esta funcao recebe uma posicao e retorna a sua linha (1, 2, 3).
    :param p: (tuple) posicao - unico parametro
    :return: (string) linha
    """
    return p[1]

def eh_posicao(arg):
    """
    Esta funcao recebe um argumento de qualquer tipo e retorna True caso este
    seja uma posicao e False caso contrario, sem nunca gerar erros.
    :param arg: (qualquer tipo) - unico parametro
    :return: (bool) True se for posicao
    """
    if type(arg)!=tuple or len(arg)!=2:
        return False
    if type(arg[0])!=str or type(arg[1])!=str:
        return False
    if len(arg[0])!=1 or len(arg[1])!=1:
        return False
    return arg[0] in ('a','b','c') and arg[1] in ('1', '2', '3')

def posicoes_iguais(p1,p2):
    """
    Esta funcao recebe duas posicoes e retorna True caso estas sejam iguais
    e False caso contrario.
    No caso de algum dos argumentos passados nao ser uma posicao, a funcao
    retorna False.
    :param p1: (tuple) primeiro parametro
    :param p2: (tuple) segundo parametro
    :return: (bool) True se forem posicoes iguais
    """
    if not eh_posicao(p1) or not eh_posicao(p2):
        return False
    return obter_pos_c(p1)==obter_pos_c(p2) and obter_pos_l(p1)==obter_pos_l(p2)

def posicao_para_str(p):
    """
    Esta funcao recebe uma posicao (representacao escolhida - tuple) e retorna
    a posicao no tipo string.
    :param p: (tuple) posicao - unico parametro
    :return: (string) posicao
    """
    return str(obter_pos_c(p))+str(obter_pos_l(p))

def obter_posicoes_adjacentes(p):
    """
    Esta funcao recebe uma posicao e retorna todas as suas posicoes adjacentes.
    :param p: (tuple) posicao - unico parametro
    :return: (tuple) posicoes adjacentes
    """
    if p==cria_posicao('a', '1'): return (cria_posicao('b','1'), cria_posicao('a','2'), cria_posicao('b','2'))
    if p==cria_posicao('b', '1'): return (cria_posicao('a','1'), cria_posicao('c','1'), cria_posicao('b','2'))
    if p==cria_posicao('c', '1'): return (cria_posicao('b','1'), cria_posicao('b','2'), cria_posicao('c','2'))
    if p==cria_posicao('a', '2'): return (cria_posicao('a','1'), cria_posicao('b','2'), cria_posicao('a','3'))
    if p==cria_posicao('b', '2'): return (cria_posicao('a','1'), cria_posicao('b','1'), cria_posicao('c','1'),
                                          cria_posicao('a','2'), cria_posicao('c','2'), cria_posicao('a','3'),
                                          cria_posicao('b','3'), cria_posicao('c','3'))
    if p==cria_posicao('c', '2'): return (cria_posicao('c','1'), cria_posicao('b','2'), cria_posicao('c','3'))
    if p==cria_posicao('a', '3'): return (cria_posicao('a','2'), cria_posicao('b','2'), cria_posicao('b','3'))
    if p==cria_posicao('b', '3'): return (cria_posicao('b','2'), cria_posicao('a','3'), cria_posicao('c','3'))
    if p==cria_posicao('c', '3'): return (cria_posicao('b','2'), cria_posicao('c','2'), cria_posicao('b','3'))
    return ()

def cria_peca(s):
    """
    Esta funcao recebe um argumento e devolve uma peca de acordo com a
    representacao escolhida (string).
    Gera erro se o argumento for diferente de X, O ou peca livre (' ').
    :param s: (argumento) unico parametro
    :return: (string) peca
    """
    if s!='X' and s!='O' and s!=' ':
        raise ValueError('cria_peca: argumento invalido')
    return s

def cria_copia_peca(j):
    """
    Esta funcao recebe uma peca e retorna outra peca, que e a copia da primeira.
    :param j: (string) peca - unico parametro
    :return: (string) peca copiada
    """
    return cria_peca(j)

def eh_peca(arg):
    """
    Esta funcao recebe um argumento de qualquer tipo e retorna True
    caso este seja uma peca e False caso contrario
    :param arg: (qualquer tipo) - unico parametro
    :return: (bool) True se for posicao
    """
    return isinstance(arg,str) and len(arg)==1

def pecas_iguais(j1,j2):
    """
    Esta funcao recebe duas pecas e retorna True caso estas sejam iguais
    e False caso contrario. Se algum dos argumentos passados nao corresponder
    a uma peca, a funcao retorna False.
    :param j1: (string) primeiro parametro
    :param j2: (string) segundo parametro
    :return: (bool) True se as pecas forem iguais
    """
    if eh_peca(j1)==True and eh_peca(j2)== True: return j1==j2
    else: return False

def peca_para_str(j):
    """
    Esta funcao recebe uma peca com a representacao escolhida (string)
    e devolve uma peca do tipo string.
    :param j: (string) peca
    :return: (string) peca
    """
    return '[{}]'.format(j)

def peca_para_inteiro(j):
    """
    Esta funcao recebe um string correspondente a uma peca e retorna
    o seu inteiro correspondente.
    1 se a peca for X, -1 se a peca for O e 0 se for uma peca livre.
    :param j: (string) peca
    :return: (inteiro) peca - 1,-1 ou 0
    """
    if pecas_iguais(j, cria_peca('X')): return 1
    if pecas_iguais(j, cria_peca('O')): return -1
    if pecas_iguais(j, cria_peca(' ')): return 0

def cria_tabuleiro():
    """
    Esta funcao nao recebe argumentos e cria um tabuleiro (lista) com
    todas as pecas vazias.
    :return: (lista) tabuleiro com pecas vazias
    """
    tab=[]
    for i in range(1,10):
        tab+=cria_peca(' ')
    return tab

def cria_copia_tabuleiro(t):
    """
    Esta funcao recebe um tabuleiro e retorna uma copia do mesmo.
    :param t: (lista) tabuleiro - unico parametro
    :return: (lista) tabuleiro copiado
    """
    copiatab=[]
    for i in t:
        copiatab+=i
    return copiatab

def obter_pos(p):
    """
    Funcao auxiliar, que recebe uma posicao representada por a1, ..., c3
    e retorna um inteiro correspondente a essa posicao, mas representado
    por algarismos de 0 a 8.
    :param p: (tuple) posicao - unico parametro
    :return: (inteiro) posicao de 0 a 8
    """
    c = obter_pos_c(p)
    l = obter_pos_l(p)
    coluna = ord(c) - ord('a') # gera um inteiro de 0 a 2 correspondente a coluna
    linha = int(l)
    linha = linha - 1 # gera um inteiro de 0 a 2 correspondente a linha
    pos = coluna + linha * 3
    return pos

def obter_peca(t,p):
    """
    Esta funcao recebe um tabuleiro e uma posicao e retorna a peca
    que esta presente na posicao passada.
    :param t: (lista) primeiro parametro
    :param p: (tuple) segundo parametro
    :return: (string) peca da posicao
    """
    pos = obter_pos(p)
    return cria_peca(t[pos])

def obter_vetor(t,s):
    """
    Esta funcao recebe um tabuleiro e um string correspondente a uma linha
    ou coluna do mesmo e retorna um tuplo com todas as pecas presentes no
    vetor indicado.
    :param t: (lista) primeiro parametro
    :param s: (string) segundo parametro
    :return: (tuple) pecas do vetor
    """
    vetor=()
    posicao=1
    if s=='a' or s=='b' or s=='c':
        while posicao <=3:
            postr=str(posicao)
            vetor+=(obter_peca(t,cria_posicao(s,postr))),
            posicao+=1
    if s=='1' or s=='2' or s=='3':
        coluna=0
        linha=int(s)-1
        while coluna<=2:
            vetor+=(t[coluna+linha*3]),
            coluna+=1  
    return vetor

def coloca_peca(t,j,p):
    """
    Esta funcao recebe um tabuleiro, um string correspondente a um jogador
    e uma posicao e coloca a peca do jogador na posicao pretendida.
    Retorna um tabuleiro com a peca colocada.
    :param t: (lista) primeiro parametro
    :param j: (string) segundo parametro
    :param p: (tuple) terceiro parametro
    :return: (lista) tabuleiro com a peca colocada
    """
    pos=obter_pos(p)
    t[pos] = j
    return t

def remove_peca(t, p):
    """
    Esta funcao recebe um tabuleiro e uma posicao da qual se pretende
    remover a peca.
    Retorna outro tabuleiro com a peca retirada.
    :param t: (lista) primeiro parametro
    :param p: (tuple) segundo parametro
    :return: (lista) tabuleiro sem a peca
    """
    pos= obter_pos(p)
    t[pos]=cria_peca(' ')
    return t

def move_peca(t, p1, p2):
    """
    Esta funcao permite deslocar uma peca, de uma posicao p1 para uma posicao p2.
    Recebe um tabuleiro e 2 posicoes, a posicao inicial, da qual pretendemos tirar a
    peca e a posicao final para a qual pretendemos deslocar a peca.
    :param t: (lista) primeiro parametro
    :param p1: (tuple) segundo parametro
    :param p2: (tuple) terceiro parametro
    :return: (lista) tabuleiro com a peca deslocada
    """
    if posicoes_iguais(p1,p2):
        return t
    else:
        coloca_peca(t, obter_peca(t, p1), p2)
        remove_peca(t, p1)
        return t

def vencedores(t):
    """
    Esta funcao recebe um tabuleiro e retorna um tuplo com todos os
    vencedores que existem no mesmo.
    Funcao auxiliar ao eh_tabuleiro, visto que num tabuleiro so pode
    existir um vencedor ao mesmo tempo.
    :param t: (lista) tabuleiro - unico parametro
    :return: (tuple) todos os vencedores
    """
    tab = 'abc123'
    for linha in tab:
        vetor = obter_vetor(t, linha)
        casasO = 0
        casasX = 0
        for posicao in vetor:
            if pecas_iguais(cria_peca('O'), posicao):
                casasO += 1
            elif pecas_iguais(cria_peca('X'), posicao):
                casasX += 1
        if (casasO == 3):
            return cria_peca('O')
        if (casasX == 3):
            return cria_peca('X')
    return cria_peca('')


def eh_tabuleiro(arg):
    """
    Esta funcao recebe um argumento e devolve True se este corresponder
    a um tabuleiro e false caso contrario.
    :param arg: (qualquer tipo) - unico parametro
    :return: (bool) True se for tabuleiro
    """
    if type(arg)!=list or len(arg)!=9:
        return False
    for i in arg:
        if not eh_peca(i):
            return False
    contaX, contaO, contanada = 0, 0, 0
    if len(vencedores(arg))>1:
        return False
    for i in arg:
        if pecas_iguais(i, cria_peca('X')): contaX+=1
        if pecas_iguais(i, cria_peca('O')): contaO+=1
    menor = min(contaX,contaO)
    maior = max(contaX,contaO)
    return contaX<=3 and contaO<=3 and (menor==maior or menor+1==maior) #ou o menor e igual ao maior ou a diferenca tem
                                                                        # de ser 1

def eh_posicao_livre(t, p):
    return pecas_iguais(obter_peca(t,p), cria_peca(' '))

def tabuleiros_iguais(t1,t2):
    """
    Esta funcao recebe dois tabuleiros e retorna True caso estes sejam
    iguais e false caso contrario.
    :param t1: (lista) tabuleiro
    :param t2: (lista) tabuleiro
    :return: (bool) True se tabuleiros iguais
    """
    colunas='abc'
    linhas='123'
    if not eh_tabuleiro(t1) or not eh_tabuleiro(t2):
        return False
    else:
        for c in colunas:
            for l in linhas:
                if pecas_iguais(obter_peca(tab1, cria_posicao(c, l)), obter_peca(tab2, cria_posicao(c, l)))==False:
                    return False
        return True


def tabuleiro_para_str(t):
    """
    Esta funcao recebe um tabuleiro e retorna o mesmo tabuleiro com
    representacao em string (ja do modo que vai estar no jogo).
    :param t: (lista) tabuleiro - unico parametro
    :return: (string) tabuleiro
    """
    t = '   a   b   c\n1 ' + peca_para_str(obter_peca(t,cria_posicao('a','1')))\
    + '-' + peca_para_str(obter_peca(t,cria_posicao('b', '1'))) + '-' + \
    peca_para_str(obter_peca(t,cria_posicao('c','1'))) + '\n   | \\ | / |\n2 ' + \
    peca_para_str(obter_peca(t,cria_posicao('a','2'))) + '-' + \
    peca_para_str(obter_peca(t, cria_posicao('b','2'))) + '-' + \
    peca_para_str(obter_peca(t, cria_posicao('c', '2'))) + '\n   | / | \\ |\n3 ' + \
    peca_para_str(obter_peca(t, cria_posicao('a', '3'))) + '-' + \
    peca_para_str(obter_peca(t, cria_posicao('b', '3'))) + '-' + \
    peca_para_str(obter_peca(t, cria_posicao('c', '3')))
    return t

def tuplo_para_tabuleiro(t):
    """
    Esta funcao recebe um tuplo correspondente a um tabuleiro e passa-o
    para a representacao de tabuleiro escolhida.
    :param t: (tuplo) tabuleiro - unico parametro
    :return: (lista) tabuleiro
    """
    tabuleiro=[]
    for i in range(0,3):
        for j in t[i]:
            if j==1:
                tabuleiro+=cria_peca('X')
            if j==-1:
                tabuleiro+=cria_peca('O')
            if j==0:
                tabuleiro+=cria_peca(' ')
    return tabuleiro

def obter_ganhador(t):
    """
    Recebe um tabuleiro e retorna uma peca correspondente a um jogador
    vencedor, se este existir.
    Caso nao exista retorna uma peca livre.
    :param t: (lista) tabuleiro
    :return: (string) jogador vencedor
    """
    tab = 'abc123'
    for linha in tab:
        vetor = obter_vetor(t,linha)
        casasO=0
        casasX=0
        for posicao in vetor:
            if pecas_iguais(cria_peca('O'), posicao):
                casasO+=1
            elif pecas_iguais(cria_peca('X'), posicao):
                casasX+=1
        if (casasO==3):
            return cria_peca('O')
        if (casasX==3):
            return cria_peca('X')
    return cria_peca('')


def obter_posicoes_livres(t):
    """
    Esta funcao recebe um tabuleiro e retorna um tuplo com todas
    as posicoes que se encontram livres.
    :param t: (lista) tabuleiro - unico parametro
    :return: (tuple) posicoes livres
    """
    posicoes =(cria_posicao('a', '1'), cria_posicao('b', '1'), cria_posicao('c', '1'), cria_posicao('a', '2'),
                cria_posicao('b', '2'), cria_posicao('c', '2'), cria_posicao('a', '3'), cria_posicao('b', '3'),
                cria_posicao('c', '3'))
    posicoes_livres=()
    for i in posicoes:
        if eh_posicao_livre(t, i):
            posicoes_livres+=(i),
    return posicoes_livres

def obter_posicoes_jogador(t,j):
    """
    Esta funcao recebe um tabuleiro e uma peca correspondente a um jogador
    e retorna um tuplo com todas as posicoes ocupadas pelo jogador.
    :param t: (lista) primeiro parametro
    :param j: (string) segundo parametro
    :return: (tuple) posicoes do jogador
    """
    posicoes=(cria_posicao('a','1'), cria_posicao('b','1'), cria_posicao('c','1'), cria_posicao('a','2'),
              cria_posicao('b','2'), cria_posicao('c', '2'), cria_posicao('a','3'), cria_posicao('b','3'),
              cria_posicao('c','3'))
    posicoes_ocupadas=()
    for i in posicoes:
        if pecas_iguais(obter_peca(t,i),j):
            posicoes_ocupadas+=(i),
    return posicoes_ocupadas

def muda_posicao(p):
    """
    Funcao auxiliar que passa uma string correspondente a uma posicao
    para uma posicao de acordo com a representacao escolhida.
    :param p: (string) posicao - unico parametro
    :return: (tuple) posicao
    """
    coluna =obter_pos_c(p)
    linha = obter_pos_l(p)
    return cria_posicao(coluna,linha)

def obter_movimento_manual(t,p):
    """
    Funcao para a jogabilidade do jogador.
    Recebe um tabuleiro e uma peca correspondente a um jogador e retorna
    uma posicao ou um movimento, consoante o numero de pecas ja em jogo.
    Gera erro se o input passado nao corresponder a uma posicao ou movimento.
    :param t: (lista) primeiro parametro
    :param p: (string) segundo parametro
    :return: (tuple) posicao ou movimento
    """
    if len(obter_posicoes_jogador(t, p))<3:
        posicao=input('Turno do jogador. Escolha uma posicao: ')
        if len(posicao)!=2 or isinstance(posicao,str)!=True or\
            posicao[0] not in ('a','b','c') or posicao[1] not in ('1', '2', '3'):
            raise ValueError('obter_movimento_manual: escolha invalida')
        pos = muda_posicao(posicao)
        if eh_posicao_livre(t, pos)!=True: raise ValueError('obter_movimento_manual: escolha invalida')
        else: return pos,
    else:
        movimento=input('Turno do jogador. Escolha um movimento: ')
        if len(movimento)!=4: # se nao tiver 4 caracteres nao e movimento, logo gera erro
            raise ValueError('obter_movimento_manual: escolha invalida')
        posicaoinicial, posicaofinal, jogalivre=movimento[:2], movimento[2:], ()
        if  type(posicaoinicial)!=str or posicaoinicial[0] not in ('a','b','c') or\
            posicaoinicial[1] not in ('1','2','3') or type(posicaofinal)!=str or\
            posicaofinal[0] not in ('a', 'b', 'c') or posicaofinal[1] not in ('1', '2', '3'):
            raise ValueError('obter_movimento_manual: escolha invalida')
        if not pecas_iguais(obter_peca(t, muda_posicao(posicaoinicial)),p):
            raise ValueError('obter_movimento_manual: escolha invalida')
        else:
            posinicial=muda_posicao(posicaoinicial)
            posfinal=muda_posicao(posicaofinal)
            movimentacao=posinicial,posfinal
            if posicoes_iguais(posinicial,posfinal): # se as posicoes sao iguais verificamos se nao ha movimento possivel
                for i in obter_posicoes_jogador(t, p):
                    for j in obter_posicoes_adjacentes(i):
                        if eh_posicao_livre(t,j):
                            jogalivre+=(i),
                if len(jogalivre)==0: return movimentacao # se nao ha, retornamos o movimento escolhido
                else: raise ValueError('obter_movimento_manual: escolha invalida') #se ha, gera erro
            if not pecas_iguais(obter_peca(t,posicaoinicial), p): # se a peca nao e dele, erro
                raise ValueError('obter_movimento_manual: escolha invalida')
            if eh_posicao_livre(t, posicaofinal)!=True: raise ValueError('obter_movimento_manual: escolha invalida')
            if posfinal not in obter_posicoes_adjacentes(posinicial):
                raise ValueError('obter_movimento_manual: escolha invalida')
            else: return movimentacao

def vitoria(t,p):
    """
    Funcao auxiliar utilizada pelo bot na fase de colocacao.
    Esta funcao recebe um tabuleiro e uma peca correspondente ao bot e retorna
    uma posicao vencedora, ou seja, se o bot conseguir formar um 3 em linha na
    jogada seguinte, esta funcao retorna a posicao necessaria para que isto
    aconteca.
    :param t: (lista) tabuleiro
    :param p: (string) peca
    :return: (tuple) posicao
    """
    poslivres=obter_posicoes_livres(t)
    for i in poslivres:
        novotab = cria_copia_tabuleiro(t)
        if pecas_iguais(obter_ganhador(coloca_peca(novotab,p,i)),p):
            return i,
    return False

def bloqueio(t,p):
    """
    Funcao auxiliar da fase de colocacao do bot.
    Recebe um tabuleiro e uma peca correspondente ao bot e retorna uma posicao
    de bloqueio, ou seja, se o oponente puder formar 3 em linha na jogada seguinte,
    o bot vai bloquear essa jogada.
    :param t: (lista) primeiro parametro
    :param p: (string) segundo parametro
    :return: (tuple) posicao
    """
    if pecas_iguais(p,cria_peca('X')):
        oponente=cria_peca('O')
    else:
        oponente=cria_peca('X')
    poslivres=obter_posicoes_livres(t)
    for i in poslivres:
        novotab=cria_copia_tabuleiro(t)
        if pecas_iguais(obter_ganhador(coloca_peca(novotab,oponente,i)),oponente):
            return i,
    return False

def centro(t):
    """
    Funcao auxiliar para a fase de colocacao do bot.
    Recebe um tabuleiro e retorna a posicao central se
    esta se encontrar livre.
    :param t: (lista) tabuleiro - unico parametro
    :return: (tuple) posicao
    """
    if eh_posicao_livre(t,cria_posicao('b','2')):
        return cria_posicao('b','2'),
    return False

def canto(t):
    """
    Funcao auxiliar para a fase de colocacao do bot.
    Recebe um tabuleiro e retorna um canto que se
    encontre livre.
    :param t: (lista) tabuleiro - unico parametro
    :return: (tuple) posicao
    """
    cantos=()
    poslivres=obter_posicoes_livres(t)
    for i in poslivres:
        if posicoes_iguais(i,cria_posicao('a','1')) or posicoes_iguais(i,cria_posicao('c','1'))\
            or posicoes_iguais(i,cria_posicao('a','3')) or posicoes_iguais(i,cria_posicao('c','3')):
            cantos += (i),
    if len(cantos) > 0:
        return cantos[0],
    return False

def lateral(t):
    """
    Funcao auxiliar para a fase de colocacao do bot.
    Recebe um tabuleiro e retorna uma posicao lateral que se
    encontre livre.
    :param t: (lista) tabuleiro - unico parametro
    :return: (tuple) posicao
    """
    laterais = ()
    poslivres = obter_posicoes_livres(t)
    for i in poslivres:
        if posicoes_iguais(i,cria_posicao('b', '1')) or posicoes_iguais(i,cria_posicao('a', '2'))\
            or posicoes_iguais(i,cria_posicao('c', '2')) or posicoes_iguais(i,cria_posicao('b', '3')):
            laterais += (i),
    if len(laterais) > 0:
        return laterais[0],
    return False

def facil(t,p):
    """
    Funcao que recebe um tabuleiro e uma peca correspondente a um jogador
    e retorna o movimento que o jogador deve executar.
    Este movimento consiste em deslocar a primeira peca que tenha uma peca
    adjacente livre.
    Se isto nao acontecer com nenhuma das pecas e possivel passar a vez,
    selecionando uma peca ocupada pelo jogador, seguida dessa mesma peca.
    :param t: (lista) primeiro parametro
    :param p: (string) segundo parametro
    :return: (tuple) movimento
    """
    for i in obter_posicoes_jogador(t, p):
        for j in obter_posicoes_adjacentes(i):
            if eh_posicao_livre(t, j):
                return i,j
    return obter_posicoes_jogador(t,p)[0], obter_posicoes_jogador(t,p)[0]

def minimax(t,j,p,seq_movimentos):
    """
    Esta e uma funcao recursiva que recebe um tabuleiro, uma peca de um jogador,
    um nivel de profundidade e uma sequencia de movimentos e retorna a sequencia de
    movimentos a ser executada pelo bot, de modo a obter uma jogada vencedora.
    A funcao analisa todos os possiveis movimentos e atraves de um algoritmo
    retorna a melhor sequencia de movimentos a executar.
    O nivel de profundidade passado dita a quantidade de movimentos que o algoritmo
    preve.
    :param t: (lista) primeiro parametro
    :param j: (string) segundo parametro
    :param p: (inteiro) terceiro parametro
    :param seq_movimentos: (tuple) quarto parametro
    :return: (tuple) sequencia de movimentos a executar
    """
    melhor_seq_movimentos=None
    if pecas_iguais(obter_ganhador(t), cria_peca('X')) or pecas_iguais(obter_ganhador(t), cria_peca('O')) or p==0:
        return peca_para_inteiro(obter_ganhador(t)), seq_movimentos
    else:
        melhor_resultado=peca_para_inteiro(cria_peca('X')) if pecas_iguais(j, cria_peca('O')) else peca_para_inteiro(cria_peca('O'))
        for i in obter_posicoes_jogador(t,j):
            for k in obter_posicoes_adjacentes(i):
                if eh_posicao_livre(t, k)==True:
                    novo_tab=cria_copia_tabuleiro(t)
                    novo_tab_mov=move_peca(novo_tab,i,k)
                    novo_resultado, nova_seq_movimentos = \
                        minimax(novo_tab_mov, cria_peca('X') if j=='O' else cria_peca('O'), p-1,
                                seq_movimentos+(i,k))
                    if melhor_seq_movimentos==None or (pecas_iguais(cria_peca('X'),j) and
                                                       novo_resultado>melhor_resultado) or\
                        (pecas_iguais(cria_peca('O'), j) and novo_resultado<melhor_resultado):
                            melhor_resultado=novo_resultado
                            melhor_seq_movimentos=nova_seq_movimentos
        return melhor_resultado, melhor_seq_movimentos

def normal(t,p):
    """
    Esta funcao recebe um tabuleiro e um string correspondente a um jogador
    e retorna um tuplo correspondente a uma posicao.
    Utiliza o algoritmo minimax com nivel de profundidade 1.
    Utilizada para realizar o movimento automatico do bot.
    :param t: (lista) primeiro parametro
    :param p: (string) segundo parametro
    :return: (tuple) movimento
    """
    return minimax(t,p,1,())[1][:2]

def dificil(t,p):
    """
    Esta funcao recebe um tabuleiro e um string correspondente a um jogador
    e retorna um tuplo correspondente a um movimento.
    Utiliza o algoritmo minimax com nivel de profundidade 5.
    Utilizada para realizar o movimento automatico do bot.
    :param t: (lista) primeiro parametro
    :param p: (string) segundo parametro
    :return: (tuple) movimento
    """
    return minimax(t,p,5,())[1][:2]

def obter_movimento_auto(t,p,dificuldade):
   """
   Esta funcao recebe um tabuleiro, um string correspondente a um jogador
   e uma cadeia de caracteres correspondente a um nivel de dificuldade que o bot
   vai aplicar no jogo e retorna uma posicao ou um movimento, dependendo da quantidade
   de pecas ja em jogo.
   As estrategias utilizam algumas das funcoes auxiliares criadas antes.
   :param t: (lista) primeiro parametro
   :param p: (string) segundo parametro
   :param dificuldade: (string) terceiro parametro
   :return: (tuple) posicao
   """
   if len(obter_posicoes_jogador(t,p))<3:
      if vitoria(t,p):
          return vitoria(t,p)
      if bloqueio(t,p):
          return bloqueio(t,p)
      if centro(t):
          return centro(t)
      if canto(t):
          return canto(t)
      if lateral(t):
          return lateral(t)
   if len(obter_posicoes_jogador(t,p))==3:
       if dificuldade=='facil':
           return facil(t,p)
       if dificuldade=='normal':
           return normal(t,p)
       if dificuldade=='dificil':
           return dificil(t,p)

def moinho(p,dificuldade):
    """
    Esta funcao recebe duas cadeias de caracteres, uma peca, '[X]' ou '[O]'
    e um nivel de dificuldade, facil, normal ou dificil, e retorna sucessivamente
    cadeias de caracteres correspondentes a tabuleiros e no final uma
    cadeia de caracteres correspondente ao vencedor do jogo.
    Gera erro se o jogador nao for '[X]' e '[O]' ou se a dificuldade nao for
    facil, normal ou perfeito.
    :param jog:(string) primeiro parametro
    :param estrategia:(string) segundo parametro
    :return:(string)tabuleiros sucessivos e vencedor ou empate
    """
    if type(p)!=str or type(dificuldade)!=str or p not in('[X]', '[O]') or dificuldade not in\
            ('facil', 'normal', 'dificil'):
        raise ValueError('moinho: argumentos invalidos')
    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade', dificuldade+ '.')
    t = cria_tabuleiro()
    print(tabuleiro_para_str(t))
    if p=='[X]':
        while pecas_iguais(obter_ganhador(t), cria_peca(' ')):
            if len(obter_posicoes_jogador(t, cria_peca('X'))) < 3:
                posicao = obter_movimento_manual(t, cria_peca('X'))[0]
                t = coloca_peca(t, cria_peca('X'), posicao)
            else:
                movimento = obter_movimento_manual(t, cria_peca('X'))
                pos1, pos2 = movimento[0], movimento[1]
                t = move_peca(t, pos1, pos2)
            print(tabuleiro_para_str(t))
            if pecas_iguais(obter_ganhador(t), cria_peca('X')): return peca_para_str(cria_peca('X'))
            if pecas_iguais(obter_ganhador(t), cria_peca('O')): return peca_para_str(cria_peca('O'))
            print('Turno do computador (' + dificuldade + '):')
            if len(obter_posicoes_jogador(t, cria_peca('O'))) < 3:
                posicao = obter_movimento_auto(t, cria_peca('O'), dificuldade)[0]
                t = coloca_peca(t, cria_peca('O'), posicao_para_str(posicao))
            else:
                movimento = obter_movimento_auto(t, cria_peca('O'), dificuldade)
                t = move_peca(t, posicao_para_str(movimento[0]), posicao_para_str(movimento[1]))
            print(tabuleiro_para_str(t))
            if pecas_iguais(obter_ganhador(t), cria_peca('X')): return peca_para_str(cria_peca('X'))
            if pecas_iguais(obter_ganhador(t), cria_peca('O')): return peca_para_str(cria_peca('O'))
    if p=='[O]':
        while pecas_iguais(obter_ganhador(t), cria_peca(' ')):
            if len(obter_posicoes_jogador(t, cria_peca('X'))) < 3:
                print('Turno do computador (' + dificuldade + '):')
                posicao = obter_movimento_auto(t, cria_peca('X'), dificuldade)[0]
                t = coloca_peca(t, cria_peca('X'), posicao_para_str(posicao))
            else:
                print('Turno do computador (' + dificuldade + '):')
                movimento = obter_movimento_auto(t, cria_peca('X'), dificuldade)
                t = move_peca(t, posicao_para_str(movimento[0]), posicao_para_str(movimento[1]))
            print(tabuleiro_para_str(t))
            if pecas_iguais(obter_ganhador(t), cria_peca('X')): return peca_para_str(cria_peca('X'))
            if pecas_iguais(obter_ganhador(t), cria_peca('O')): return peca_para_str(cria_peca('O'))
            if len(obter_posicoes_jogador(t, cria_peca('O'))) < 3:
                posicao = obter_movimento_manual(t, cria_peca('O'))[0]
                t = coloca_peca(t, cria_peca('O'), posicao)
            else:
                movimento = obter_movimento_manual(t, cria_peca('O'))
                pos1, pos2 = movimento[0], movimento[1]
                t = move_peca(t, pos1, pos2)
            print(tabuleiro_para_str(t))
            if pecas_iguais(obter_ganhador(t), cria_peca('X')): return peca_para_str(cria_peca('X'))
            if pecas_iguais(obter_ganhador(t), cria_peca('O')): return peca_para_str(cria_peca('O'))
print(moinho("[X]", "normal"))

