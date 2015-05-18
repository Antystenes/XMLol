
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Tabelka lol</h2>
  <table border="3">
    <tr bgcolor="#9acd32">
      <th>Imię</th>
      <th>Nazwisko</th>
    </tr>
    <xsl:for-each select="data/osoba">
    <tr>
      <td><xsl:value-of select="data/osoba/name"/></td>
      <td><xsl:value-of select="data/osoba/surname"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>