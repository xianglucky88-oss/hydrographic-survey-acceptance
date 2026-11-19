# 港湾测深成果验收

为测绘资料接收方保存测线、覆盖、基准、底质和通航孔的成果事实。输入坐标与高程已转换至样本所声明的工程坐标和基准。

数据工程子方向为**数仓与数据湖**。基线接收已整理为 UTF-8 JSON 的合成业务数据，按数据链独立产出 JSON 事实。仓库根目录可直接运行，运行时和测试使用 Python 3.11 或以上的标准库。

## 运行

```sh
python3 -m hydrographic_survey_acceptance crosslines examples/crosslines.json
python3 -m hydrographic_survey_acceptance crosslines examples/crosslines.json --sqlite facts.sqlite
python3 -m unittest discover -s tests -v
```

Python 调用入口为 `process(pipeline, data)`。命令行也可以将 JSON 结果输出到标准输出。选用 SQLite 时，`runs` 保留原始 JSON 及 SHA-256，`facts` 保留每项具名事实和对应批次。每个输入按规范化 JSON 的摘要标识，同一处理链重复导入同一输入只保留一批；输入或处理失败时不会留下半批结果。处理逻辑改版后的重算应使用独立结果库。

## 数据链与离线样本

| 数据链 | 基线行为 | 试样 |
|---|---|---|
| `crosslines` | 比较已配对且使用同一基准的主测线和复核线深度。 | `examples/crosslines.json` |
| `swath-coverage` | 统计各验收格是否被声明的名义扫幅命中。 | `examples/swath-coverage.json` |
| `tide-reference` | 用同一已知零点差换算单个水尺序列的水位。 | `examples/tide-reference.json` |
| `bottom-grabs` | 将底质实验室的各粒级质量归一成质量占比。 | `examples/bottom-grabs.json` |
| `bridge-clearance` | 根据已指定的单个控制构件和参考水位计算净空。 | `examples/bridge-clearance.json` |

活动口径来自各样本。样例记录的业务标识用作事实键或保留在结果中。`tests/expected` 中的结果只描述这些基线试样。合成数据和示例规则用于开发验证，实际签发、专业判定及合规认证需采用对应项目的正式数据与规则。
