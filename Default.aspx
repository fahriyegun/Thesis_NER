<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        .auto-style1 {
            width: 101px;
        }
        </style>
    </head>
<body style="height: 839px">
    <form id="form1" runat="server">
    <div>
        <asp:Label ID="Label11" runat="server" Text=""></asp:Label>
        <table style="height: 59px; width: 441px">
            <tr>
                <th class="auto-style1">
                    <asp:Label ID="Label1" runat="server" Text="E-Mail"></asp:Label>
                </th>
                <th>                    
                    <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>                    
                </th>
                <th>
                    <asp:Button ID="getBtn" runat="server" Text="Tweet al" OnClick="Button1_Click1" Width="96px" />
                </th>
            </tr>
        </table>
        <table>
            <tr></tr>
        </table>
        <table>
           
        </table>
        <asp:Label ID="Label10" runat="server" Text=""></asp:Label>
        <asp:Table ID="Table1" runat="server"></asp:Table>
        <table>
            <tr>
                <th>
                    <asp:Button ID="prevBtn" runat="server" Text="Önceki Tweete Dön" OnClick="prevBtn_Click" />
                </th>
                <th>
                    <asp:Button ID="nextBtn" runat="server" Text="Sıradaki Tweet" OnClick="nextBtn_Click" />
                </th>
            </tr>
        </table>
      
        <asp:Button ID="sonlandırButton" runat="server" style="margin-left: 51px" Text="Sonlandır" Width="153px" OnClick="sonlandırButton_Click" />
      
    </div>

    </form>
</body>
</html>
