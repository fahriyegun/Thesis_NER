using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Web;
using System.Web.UI;
using System.Web.UI.HtmlControls;
using System.Web.UI.WebControls;

public partial class _Default : System.Web.UI.Page
{
    static int sentenceNumber = 0;
    static string textFull;
    static string[] sentences;
    string[] words;
    string[] wordsplit;
    static string[] wordlist;
    static RadioButton[] rb;
    TableRow satir;
    TableCell sutun;
    RadioButtonList[] blist;
    static int index = 0;
    static string email;
    string connectionString = "server=FAHRIYEGUN\\SQLEXPRESS; Initial Catalog=tagTableDB;Integrated Security=SSPI";

    protected void Page_Load(object sender, EventArgs e)
    {
        prevBtn.Visible = false;
        nextBtn.Visible = false;
        sonlandırButton.Visible = false;
   
    }

    //tweet al BUTTON CLICK
    public void Button1_Click1(object sender, EventArgs e)
    {
        email = TextBox1.Text;

        if (string.IsNullOrWhiteSpace(TextBox1.Text))
        {
            // Message box
            Label11.Text = "Lütfen e-mail adresinizi girin!";
        }
        else
        {
            Label11.Text = "";
            getTweet();
        }
    }


    public void getTweet()
    {
        prevBtn.Visible = true;
        nextBtn.Visible = true;
        sonlandırButton.Visible = true;
        TextBox1.Visible = false;
        getBtn.Visible = false;
        Label1.Visible = false;
        //dosya okuma
        string dosya_yolu = "C:\\Users\\Fahriye\\Desktop\\tweets\\tweet_1.txt";
        FileStream fs = new FileStream(dosya_yolu, FileMode.Open, FileAccess.Read);
        StreamReader sw = new StreamReader(fs);
        string yazi;
        while ((yazi= sw.ReadLine()) != null)
        {
            textFull += yazi;
            
        }
        sw.Close();
        fs.Close();
        splitSentences(0);
        Label10.Text = " Tweet: " + sentences[0];
    }

    public void nextBtn_Click(object sender, EventArgs e)
    {
        //dosya sonuna gelirse
        if (sentences.Length == (sentenceNumber+1))
        {
            keepdata();
            //db_usertable();
            Label10.Text = "Teşekkürler :)";
        }
        else
        {
            keepdata();
            prevBtn.Visible = true;
            nextBtn.Visible = true;
            sonlandırButton.Visible = true;
            sentenceNumber++;
            splitSentences(sentenceNumber);
            Label10.Text = "Tweet: " + sentences[sentenceNumber];
        }
       
        
    }
    public void keepdata()
    {
            //you can also inspect request.form colletion
            foreach (string item in Request.Form.AllKeys)
            {
                //ct ile başlayan nameler
                if (item[0] == 'c' && item[1] == 't')
                {
                    // wordsplit[0] = word and wordsplit[1] = tagtype
                    wordsplit = Regex.Split(Request.Form[item], ",");
                    db_tagtable(wordsplit);
            }
            
        }            
    }

    public void splitSentences(int sentenceNumber)
    {

        if (sentenceNumber == 0)
        {
            sentences = Regex.Split(textFull, ":");
        }

        words = Regex.Split(sentences[sentenceNumber], " ");
        yerlestir(words);
        
    }

    public void yerlestir(string[] words)
    {
        int sutunSayisi = 2;
        int satirSayisi = words.Length + 1;
        blist = new RadioButtonList[words.Length];
        String[] listItemNames = {"Person","Location","Organization","Product","Date","Money","Percent","Other"}; 
        rb = new RadioButton[(words.Length) * 8];

        for (int i = 0; i < satirSayisi; i++)
        {
            satir = new TableRow();

            for (int j = 0; j < sutunSayisi; j++)
            {
                sutun = new TableCell();

                if (i == 0)
                {
                    sutun.BorderStyle = BorderStyle.Outset;
                    if (j == 0) { sutun.Text = "Kelimeler"; }
                    else if (j == 1) { sutun.Text = "Etiket Türleri"; }
                    satir.Cells.Add(sutun);
                }
                // Kelimeler
                if (j == 0 & i != 0)
                {
                    sutun.Text = words[i - 1];
                    sutun.BorderStyle = BorderStyle.Outset;
                    satir.Cells.Add(sutun);
                }
                //Radio Button List ekle
                else if(j != 0 & i != 0)
                {
                    blist[i - 1] = new RadioButtonList();
                    foreach (String itemName in listItemNames)
                    {
                        blist[i - 1].Attributes.Add("name", "list");
                        ListItem li = new ListItem(itemName, words[i - 1] + "," + itemName);
                        //li.Attributes.Add("name","list");
                        blist[i - 1].Items.Add(li);
                        blist[i - 1].SelectedIndex = 7;
                        blist[i - 1].RepeatDirection = RepeatDirection.Horizontal;
                    }
                    sutun.Controls.Add(blist[i-1]);
                    satir.Cells.Add(sutun);
                }
            }
            Table1.Rows.Add(satir);
        }
    }

    public void db_tagtable(string[] wordsplit)
    {
        if(wordsplit[1] != "Other")
        {
            string Command = "INSERT INTO tweetli (tweet, word, tagType) VALUES (@tweet, @word, @tagType) ;";
            //INSERT INTO users (email, tweetnumber) VALUES (@email, @tweetnumber) ;";

            using (SqlConnection myConnection = new SqlConnection(connectionString))
            {
                myConnection.Open();
                //etiketlenen kelimeleri db ye at
                using (SqlCommand myCommand = new SqlCommand(Command, myConnection))
                {
                    myCommand.Parameters.AddWithValue("@tweet", sentences[sentenceNumber]);
                    myCommand.Parameters.AddWithValue("@word", wordsplit[0]);
                    myCommand.Parameters.AddWithValue("@tagType", wordsplit[1]);
                    string Result = (string)myCommand.ExecuteScalar(); // returns the first column of the first row
                }
                myConnection.Close();
            }
        }
                 
    }
    /*
    public void db_usertable()
    {
        string Command = "INSERT INTO users (email, tweetnumber) VALUES (@email, @tweetnumber) ;";

        using (SqlConnection myConnection = new SqlConnection(connectionString))
        {
            myConnection.Open();
            //userları db ye at
            using (SqlCommand myCommand = new SqlCommand(Command, myConnection))
            {
                myCommand.Parameters.AddWithValue("@email", email);
                myCommand.Parameters.AddWithValue("@tweetnumber", (sentenceNumber+1));
                string Result = (string)myCommand.ExecuteScalar(); // returns the first column of the first row
            }
            myConnection.Close();
        }
    }*/

    public void delete_tag()
    {
        string Command = "delete from tag where tag.sentencenumber = @sentencenumber; ";

        using (SqlConnection myConnection = new SqlConnection(connectionString))
        {
            myConnection.Open();
            //değişecek tweetleri sil
            using (SqlCommand myCommand = new SqlCommand(Command, myConnection))
            {
                myCommand.Parameters.AddWithValue("@sentencenumber", (sentenceNumber+1));
                string Result = (string)myCommand.ExecuteScalar(); // returns the first column of the first row
            }
            myConnection.Close();
        } 
    }

    protected void prevBtn_Click(object sender, EventArgs e)
    {
        prevBtn.Visible = true;
        nextBtn.Visible = true;
        sonlandırButton.Visible = true;
        sentenceNumber--;
        splitSentences(sentenceNumber);
        delete_tag();
        Label10.Text = sentences[sentenceNumber];
    }


    protected void sonlandırButton_Click(object sender, EventArgs e)
    {
        prevBtn.Visible = false;
        nextBtn.Visible = false;
        sonlandırButton.Visible = false;
        keepdata();
       // db_usertable();            
        Label10.Text = "Teşekkürler :)";        
    }
}