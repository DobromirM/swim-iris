package swim.iris.beans;

import com.opencsv.bean.CsvBindByName;

public class TestingRecord {

  @CsvBindByName
  private Integer index;

  @CsvBindByName
  private Float sepal_length;

  @CsvBindByName
  private Float sepal_width;

  @CsvBindByName
  private Float petal_length;

  @CsvBindByName
  private Float petal_width;

  @Override
  public String toString() {
    return "TestingRecord{" + "index=" + index + ", sepal_length=" + sepal_length + ", sepal_width=" + sepal_width + ", petal_length=" + petal_length + ", petal_width=" + petal_width + '}';
  }
}
