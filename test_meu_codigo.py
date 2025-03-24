import pytest


def primo(numero: int, * args) -> int:
    if type(numero) != int:
        raise ValueError("Variavel tem que ser do tipo int")
    if args:
        raise TypeError("A função aceita apenas um argumento")
    if numero is None:
        raise ValueError("O parametro não pode ser vazio")
    
    if numero < 2:
        return bool(False)
    i = 2
    while i * i <= numero:
        if numero % i == 0:
            return bool(False)
        i += 1
    return bool(True)

def test_garantir_que_primo_retorne_realmente_um_numero_primo_True():
    actual_result = primo(numero=2)

    assert actual_result == True

def test_se_não_for_primo_deve_retornar_False():
    actual_result = primo(numero=10)

    assert actual_result == False

def test_tem_que_ocorrer_erro_quando_o_argumento_numero_não_for_inteiro():
    with pytest.raises(ValueError):
        primo(numero="pnumero=lnumero=vra")

    with pytest.raises(ValueError):
        primo(numero=10.674)

    with pytest.raises(ValueError):
        primo(numero= True)

def test_tem_que_retornar_erro_ao_inserir_mais_de_dois_argumentos_nos_parametros():
     with pytest.raises(TypeError):
        primo(numero="pnumero=lnumero=vra", paoa = 34)

def test_tem_que_retornar_erro_ao_não_obter_argumento_algum_no_parametro():
    with pytest.raises(ValueError):
        primo(numero=None)













