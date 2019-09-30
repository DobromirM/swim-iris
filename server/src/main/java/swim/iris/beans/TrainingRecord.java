package swim.iris.beans;

import com.opencsv.bean.CsvBindByName;

public class TrainingRecord {
  
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
  
  @CsvBindByName
  private Integer label;
  
  @Override
  public String toString() {
    return "TrainingRecord{" + "index=" + index + ", sepalLength=" + sepalLength + ", sepalWidth=" + sepalWidth + ", petalLength=" + petalLength + ", petalWidth=" + petalWidth + ", label=" + label + '}';
  }
}
