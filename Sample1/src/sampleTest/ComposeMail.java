package sampleTest;

import org.testng.annotations.Test;

import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;

import org.testng.annotations.BeforeTest;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.AfterTest;

public class ComposeMail {
	WebDriver d;
	WebDriverWait w;
  @Test
  public void f() throws BiffException, IOException {
	  FileInputStream f=new FileInputStream("C:\\Users\\dell\\Desktop\\GMail TC.xls");
	  Workbook f1=Workbook.getWorkbook(f);
	  Sheet s=f1.getSheet(0);
	  String[][] td=new String[s.getColumns()][s.getRows()];
	  int r=s.getRows();
	  int c=s.getColumns();
	  for(int i=0;i<r;i++) {
		  for(int j=0;j<c;j++) {
			  td[j][i]=s.getCell(j, i).getContents();
		  }
	  }
	  for(int i=0;i<r;i++) {
		  int col=0;
		  d.findElement(By.xpath("//input[@type='email']")).sendKeys(td[col][i]);
		  d.findElement(By.xpath("//div[@class='VfPpkd-RLmnJb']")).click();
		  d.findElement(By.xpath("//input[@type='password']")).sendKeys(td[++col][i]);
		  WebElement S=d.findElement(By.xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc']"));
		  WebElement C=d.findElement(By.xpath("//div[contains(text(),'Compose')]"));
		  S.click();
		  w.until(ExpectedConditions.visibilityOf(C));
		  C.click();
		  d.findElement(By.xpath("//textarea[@name='to']")).sendKeys(td[++col][i]);
		  d.findElement(By.xpath("//input[@name='subjectbox']")).sendKeys(td[++col][i]);
		  d.findElement(By.xpath("//div[@aria-label='Message Body']")).sendKeys(td[++col][i]);
		  WebElement AF=d.findElement(By.xpath("//div[@id=':a9']"));
		  AF.sendKeys(td[++col][i]);
		  
	  }
  }
  @BeforeTest
  public void beforeTest() {
	  System.setProperty("webdriver.chrome.driver", "C:\\Program Files (x86)\\Selenium Jars\\chromedriver 88.exe");
	  d=new ChromeDriver();
	  d.manage().window().maximize();
	  d.get("https://www.gmail.com/");
	  d.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
  }

  @AfterTest
  public void afterTest() throws InterruptedException {
	  Thread.sleep(2000);
	  d.close();
  }

}
