import streamlit as st

st.set_page_config(page_title="Teste de Arquétipos - Chatbot")

# Definição das afirmações dos arquétipos
arquetipos = {
    "A": "O essencial é simples! Busco alcançar o paraíso e ser feliz. Meu direcionamento é por segurança e paz.",
    "B": "Todos os homens e mulheres são iguais! Busco fazer parte do grupo por meio da minha conexão com as pessoas. Meu direcionamento é por pertencimento e realidade.",
    "C": "Onde há uma vontade há um caminho! Busco provar meu valor por meio de ações corajosas. Meu direcionamento é por excelência e coragem.",
    "D": "AME O PRÓXIMO COMO A SI MESMO! Busco proteger e cuidar das pessoas. Meu direcionamento é por bem-estar e compaixão.",
    "E": "NÃO LEVANTE CERCAS À MINHA VOLTA! Busco liberdade para descobrir quem sou. Meu direcionamento é por liberdade e satisfação.",
    "F": "REGRAS FORAM FEITAS PARA SEREM QUEBRADAS! Busco libertação e revolução. Meu direcionamento é por risco e revolução.",
    "G": "CADA PESSOA É ÚNICA! Busco experiências de intimidade e prazer. Meu direcionamento é por paixão e compromisso.",
    "H": "SE VOCÊ PODE IMAGINAR ALGO, ISSO PODE SER FEITO! Busco criar coisas de valor duradouro. Meu direcionamento é por inovação e criatividade.",
    "I": "PODER E INFLUÊNCIA SÃO IMPORTANTES! Busco exercer a liderança. Meu direcionamento é por responsabilidade e poder.",
    "J": "EU FAÇO AS COISAS ACONTECEREM! Busco compreender as leis naturais do universo. Meu direcionamento é por consciência e transformação.",
    "K": "A VERDADE É LIBERTADORA! Busco encontrar a verdade utilizando a inteligência. Meu direcionamento é por sabedoria e verdade.",
    "L": "SÓ SE VIVE UMA VEZ! Busco me divertir e iluminar o mundo. Meu direcionamento é por diversão e leveza."
}

def chatbot():
    """Função principal do chatbot interativo."""
    st.title("Chatbot - Teste de Arquétipos")
    st.write("Bem-vindo ao Teste de Arquétipos. Responda as perguntas e descubra seu perfil!")

    # Etapa 1 - Você
    st.header("Etapa 1: Você")
    nome = st.text_input("Qual é o seu nome?")
    quem_e_voce = st.text_area("Quem é você?")
    o_que_busca = st.text_area("O que você busca?")
    qual_direcionamento = st.text_area("Qual é o seu direcionamento?")

    if st.button("Avançar para a escolha do arquétipo pessoal"):
        arquetipo_pessoal = comparar_arquetipos(list(arquetipos.keys()))
        st.session_state["arquetipo_pessoal"] = arquetipo_pessoal
        st.write("Arquétipo pessoal selecionado!")

    # Etapa 2 - Negócio
    st.header("Etapa 2: Seu Negócio")
    como_ajuda = st.text_area("Como você serve e ajuda as pessoas?")
    proposito = st.text_area("Qual o propósito do seu negócio?")

    if st.button("Avançar para a escolha do arquétipo do negócio"):
        arquetipo_negocio = comparar_arquetipos(list(arquetipos.keys()))
        st.session_state["arquetipo_negocio"] = arquetipo_negocio
        st.write("Arquétipo do negócio selecionado!")

    # Etapa 3 - Público
    st.header("Etapa 3: Seu Público")
    desejos_cliente = st.text_area("Quais são os desejos e necessidades do seu cliente ideal?")
    como_ajuda_cliente = st.text_area("Como sua marca o ajuda?")

    if st.button("Finalizar e ver resultado"):
        arquetipo_publico = comparar_arquetipos(list(arquetipos.keys()))
        st.session_state["arquetipo_publico"] = arquetipo_publico
        
        # Exibir resultado final
        st.success("Teste concluído!")
        st.write(f"**1° - Você:** {arquetipos[st.session_state['arquetipo_pessoal']]}")
        st.write(f"**2° - Negócio:** {arquetipos[st.session_state['arquetipo_negocio']]}")
        st.write(f"**3° - Público:** {arquetipos[st.session_state['arquetipo_publico']]}")

def comparar_arquetipos(opcoes):
    """Função para comparar arquétipos de forma interativa."""
    while len(opcoes) > 1:
        opcao1, opcao2 = opcoes[:2]
        escolha = st.radio("Qual afirmação melhor representa você?", [arquetipos[opcao1], arquetipos[opcao2]])
        
        if escolha == arquetipos[opcao1]:
            opcoes.remove(opcao2)
        else:
            opcoes.remove(opcao1)
    
    return opcoes[0]

if __name__ == "__main__":
    chatbot()
