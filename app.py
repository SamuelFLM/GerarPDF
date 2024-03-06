import streamlit as st
import pdfkit
import base64
import os

wkhtmltopdf_path = r"wkhtmltopdf\bin\wkhtmltopdf.exe"

# Configure o pdfkit para usar o binário
config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)


st.header("Página da web para gerar :red[PDF]")
st.caption("Converter uma página Web através da URL para PDF")
st.caption("✅Gratuito ✅Online ✅Sem limites")

with st.container(border=True):
    url_placeholder = st.empty()
    nome_arquivo_placeholder = st.empty()
    
    url = url_placeholder.text_input("URL da página a ser gerada", placeholder='https://exemplo.com')
    nome_arquivo = nome_arquivo_placeholder.text_input("Nome do arquivo", placeholder='exemplo')
    
col1, col2, col3 = st.columns([0.3,0.3,0.6])
btn = col1.button("Converter para :red[PDF]", use_container_width=True)
btn_limpar = col2.button("Limpar", use_container_width=True, type='primary')

if btn:
    try:
        with st.spinner("Gerando PDF..."):
            pdfkit.from_url(url, f"{nome_arquivo}.pdf", verbose=True, configuration=config)
        with open(f"{nome_arquivo}.pdf", "rb") as f:
                bytes = f.read()
                b64 = base64.b64encode(bytes).decode()
                href = f'<a href="data:file/pdf;base64,{b64}" download=\'{nome_arquivo}.pdf\' style="display: inline-block; padding: 10px 20px; color: #fff; background-color: #007bff; border-radius: 5px; text-decoration: none;">Clique aqui para baixar o PDF</a>'
                st.markdown(href, unsafe_allow_html=True)
    except:
        st.error("😕 Parece que seu link não aceita a geração do PDF")
    if os.path.exists(f"{nome_arquivo}.pdf"):
        os.remove(f"{nome_arquivo}.pdf")  # Remove o arquivo após o download
    
        
elif btn_limpar:
    url_placeholder.text_input("URL da página a ser gerada", value="", key='unique_key_url', placeholder='https://exemplo.com')
    nome_arquivo_placeholder.text_input("Nome do arquivo", value="", key='unique_key_nome_arquivo', placeholder='exemplo')
    

st.subheader("Perguntas Frequentes", divider=True)

with st.expander("É possível gerar PDF de todos os sites?"):
    st.markdown("Não necessariamente. Alguns sites possuem políticas de segurança rigorosas que podem resultar em um PDF gerado de maneira inadequada ou estranha.")
    
with st.expander("Quem desenvolveu?"):
    st.markdown("Desenvolvedor Full Stack - Samuel Felipe")
    st.markdown("[Linkedin](https://www.linkedin.com/in/samuelflima/)")

