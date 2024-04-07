const xml2js = require('xml2js');

const xml = `
<root>
  <item>
    <nome>Item 1</nome>
    <descricao>Descrição do Item 1</descricao>
  </item>
  <item>
    <nome>Item 2</nome>
    <descricao>Descrição do Item 2</descricao>
  </item>
</root>
`;

xml2js.parseString(xml, (err, result) => {
    if (err) {
      throw err;
    }
  

    const itens = result['root']['item']; // Acesse os itens dentro da tag 'root'

  itens.forEach(item => {
    const nome = item['nome'][0];
    const descricao = item['descricao'][0];

    const novoXml = `<item nome="${nome}" descricao="${descricao}">`;
    console.log(novoXml);
  });
});



