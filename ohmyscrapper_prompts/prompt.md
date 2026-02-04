---
model: "gemini-2.5-flash"
name: "text-job-parser"
description: "Solicita o parseamento de urls de textos enviados."
---
<contexto>Esses são textos com 1 ou várias vagas de emprego. Quando há mais de uma vaga em um texto, elas são acompanhadas de suas respectivas urls.</contexto>
<textos>
{ohmyscrapper_texts}
</textos>
<pedido>Faça uma lista em `XML` com o número de id de cada texto seguido do cargo de cada vaga. Se houver, sua respectiva organização ou empresa. Se houver, o respectivo prazo de candidatura. Se houver, o local da vaga. Se houver, o salário oferecido da vaga. Se houver, o tipo de contratação (Freelance, CLT, PJ, Full-time e etc.).</pedido>
<formato_resposta_esperado>
    Se não for possível identificar a organização ou empresa, deixe esta informação em branco.
    Se não for possível identificar a url, deixe esta informação em branco.
    Para cada vaga, mantenha o mesmo idioma em que o respectivo texto está escrito. Responda, sem informações adicionais ou explicação, apenas o texto em `XML` como o exemplo a seguir:
    <vagas>
        <vaga>
            <id>12</id>
            <cargo>Nome do Cargo da Vaga 12</cargo>
            <contratante>Nome da Empresa 12</contratante>
            <local>São Paulo (SP)</local>
            <salario>De R$ 1000 a R$ 1500</salario>
            <tipo>Full-time</tipo>
            <prazo>Até 20 de dezembro</prazo>
            <url>http://www.url-vaga-12.com/exemplo</url>
        </vaga>
        <vaga>
            <id>215</id>
            <cargo>Position Name 215</cargo>
            <contratante>Company Name 215</contratante>
            <local>Híbrido em Campinas (SP)</local>
            <salario>De R$ 2000 a R$ 4500</salario>
            <tipo>Temporário</tipo>
            <prazo>Até 15 de janeiro</prazo>
            <url>http://www.url-position-215.com/sample</url>
        </vaga>
        <vaga>
            <id>941</id>
            <cargo>Nome do Cargo da Vaga 941</cargo>
            <contratante>Nome da Empresa 941</contratante>
            <local>Remoto</local>
            <salario></salario>
            <tipo>Freelance</tipo>
            <prazo></prazo>
            <url>http://www.url-empresa-941.com/vaga</url>
        </vaga>
        <vaga>
            <id>85</id>
            <cargo>Nome do Cargo da Vaga 85</cargo>
            <contratante></contratante>
            <local>Local não informado</local>
            <salario>De R$ 1000 a R$ 1500</salario>
            <tipo>Meio período</tipo>
            <prazo>Até 01 de março</prazo>
            <url></url>
        </vaga>
    </vagas>

</formato_resposta_esperado>
