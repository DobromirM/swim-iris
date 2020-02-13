package swim.iris.beans;

import com.opencsv.bean.CsvBindByName;

public class TrainingRecord {

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

  @CsvBindByName
  private Integer label;

  @Override
  public String toString() {
    return "TrainingRecord{" + "index=" + index + ", sepal_length=" + sepal_length + ", sepal_width=" + sepal_width + ", petal_length=" + petal_length + ", petal_width=" + petal_width + ", label=" + label + '}';
  }
}
