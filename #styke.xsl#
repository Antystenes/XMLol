<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Tabelka lol</h2>
  <table border="3">

    <xsl:for-each select="data/osoba">
      <tr>
	<td>
      <xsl:value-of select="name"/><br/>
      <xsl:value-of select="surname"/><br/>
      <xsl:value-of select="sex"/><br/>
      <xsl:value-of select="dateofbirth"/><br/>
      <xsl:for-each select="number">
      <xsl:value-of select="."/><br/>
      </xsl:for-each>
	</td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>
