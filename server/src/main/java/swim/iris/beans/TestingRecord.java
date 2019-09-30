package swim.iris.beans;

import com.opencsv.bean.CsvBindByName;

public class TestingRecord {
  
  @CsvBindByName
  private Integer index;
  
  @CsvBindByName
  private Float sepalLength;
  
  @CsvBindByName
  private Float sepalWidth;
  
  @CsvBindByName
  private Float petalLength;
  
  @CsvBindByName
  private Float petalWidth;
  
  @Override
  public String toString() {
    return "TestingRecord{" + "index=" + index + ", sepalLength=" + sepalLength + ", sepalWidth=" + sepalWidth + ", petalLength=" + petalLength + ", petalWidth=" + petalWidth + '}';
  }
}
